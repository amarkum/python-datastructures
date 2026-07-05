# Facebook — System Design (Detailed)

Complete system design for the world's largest social network — social graph (TAO), ML-ranked news feed, Messenger, Groups at 3B+ user scale.

---

## 1. Requirements & Capacity

| Metric | Estimate |
|--------|----------|
| DAU | 2B |
| Friend connections | ~500B edges |
| Posts/day | 500M |
| Feed reads/day | 100B+ |
| Messages/day | 20B |
| Graph storage | 500B edges × 16B ≈ 8 PB |

---

## 2. High-Level Architecture

```mermaid
flowchart TB
    subgraph clients [3B Users]
        Mobile[Mobile Apps]
        Web[Web Browser]
    end

    subgraph edge [Edge]
        CDN[CDN - static/media]
        LB[L7 Load Balancer]
        GQL[GraphQL Gateway]
    end

    subgraph core [Core Services]
        Graph[Social Graph Service]
        Feed[News Feed Ranker]
        User[User Service]
        Messenger[Messenger Service]
        Group[Groups Service]
        Event[Events Service]
        Ads[Ads Platform]
        Search[Graph Search]
    end

    subgraph ml [ML Layer]
        Ranker[Feed Ranker ML]
        Sugg[Friend Suggestion ML]
        AdRank[Ad Ranker]
    end

    subgraph data [Data Layer]
        TAO[(TAO Graph Cache)]
        MySQL[(MySQL Sharded - graph)]
        Cassandra[(Cassandra - posts)]
        HBase[(HBase - messages)]
        Redis[(Redis/Memcached)]
        Kafka[Kafka/Scribe]
    end

    Mobile --> CDN
    Mobile --> LB --> GQL
    GQL --> Graph --> TAO --> MySQL
    GQL --> Feed --> Ranker
    Feed --> Cassandra
    Feed --> Redis
    GQL --> Messenger --> HBase
    Messenger --> Redis
    Ranker --> Kafka
    Sugg --> MySQL
    Ads --> AdRank
```

---

## 3. Social Graph — TAO Architecture

```mermaid
flowchart TB
    subgraph app [Application Layer]
        GS[Graph Service]
    end

    subgraph tao [TAO Cache Layer]
        TAO1[TAO Server 1]
        TAO2[TAO Server 2]
        TAO3[TAO Server N]
    end

    subgraph db [MySQL Shards]
        S1[(Shard 1<br/>user_id 0-1B)]
        S2[(Shard 2<br/>user_id 1B-2B)]
        S3[(Shard 3<br/>user_id 2B-3B)]
    end

    GS --> TAO1
    GS --> TAO2
    TAO1 -->|cache miss 1%| S1
    TAO2 -->|cache miss| S2
```

**TAO stores two entity types:**
```
Objects:      (user_id) → { name, profile_pic, location, ... }
Associations: (user_id) --FRIENDS--> (friend_id)
              (user_id) --MEMBER_OF--> (group_id)
              (user_id) --RSVP--> (event_id)
```

### 3.1 Graph Database Schema (MySQL)

```sql
-- Objects table (entities)
CREATE TABLE objects (
    id          BIGINT PRIMARY KEY,       -- user_id, group_id, etc.
    type        INT NOT NULL,               -- USER=1, GROUP=2, PAGE=3
    data        BLOB,                       -- serialized attributes
    created_at  TIMESTAMP,
    updated_at  TIMESTAMP
);

-- Associations table (edges in graph)
CREATE TABLE associations (
    id1         BIGINT NOT NULL,            -- source node (SHARD KEY)
    atype       INT NOT NULL,               -- FRIENDS=1, MEMBER_OF=2, LIKES=3
    id2         BIGINT NOT NULL,            -- target node
    time        TIMESTAMP DEFAULT NOW(),
    data        BLOB,                       -- edge metadata
    PRIMARY KEY (id1, atype, id2)
);

-- Indexes
CREATE INDEX idx_assoc_id2 ON associations (id2, atype);  -- reverse lookup
CREATE INDEX idx_assoc_time ON associations (id1, atype, time DESC);
```

### 3.2 Graph Indexing Strategy

| Query | Index Used | Complexity |
|-------|-----------|------------|
| Friends of user X | `(id1= X, atype=FRIENDS)` | O(log N + degree) |
| Mutual friends X,Y | Intersect friends(X) ∩ friends(X) | O(d1 + d2) |
| Groups user X belongs to | `(id1=X, atype=MEMBER_OF)` | O(log N + groups) |
| Reverse: who likes post P | `(id2=P, atype=LIKES)` | O(log N) via idx_assoc_id2 |

**Mutual friends query:**
```sql
-- Step 1: get friends of X (from TAO cache)
SELECT id2 FROM associations WHERE id1=X AND atype=FRIENDS;
-- Step 2: get friends of Y
SELECT id2 FROM associations WHERE id1=Y AND atype=FRIENDS;
-- Step 3: intersect in application layer (or bitmap for power users)
```

---

## 4. News Feed — ML Ranking Pipeline

```mermaid
flowchart TB
    Request[Feed Request] --> Candidate[Stage 1: Candidate Generation]
    Candidate --> |~500 posts| Rank[Stage 2: ML Ranking]
    Rank --> |top 50| Filter[Stage 3: Filtering]
    Filter --> |~30 posts| Cache[Stage 4: Cache in Redis]
    Cache --> Response[Return to user]

    subgraph candidates [Candidate Sources]
        F[Friends posts]
        G[Groups posts]
        P[Pages followed]
        R[Recommended ML]
    end

    candidates --> Candidate

    subgraph ml [ML Models]
        M1[P_like - predict like probability]
        M2[P_comment - predict comment]
        M3[P_share - predict share]
        Score[score = w1*P_like + w2*P_comment + w3*P_share]
    end

    ml --> Rank
```

**Feed ranking features (1000+ features):**
```
User features:    age, location, device, time_of_day, past_engagement
Post features:    author relationship, post type, recency, hashtag
Context features: session depth, network speed, battery level
Interaction history: past likes/comments on this author's posts
```

### 4.1 Feed Sequence Diagram

```mermaid
sequenceDiagram
    participant App
    participant Feed as Feed Service
    participant Redis
    participant Graph as Graph Service
    participant TAO
    participant Ranker as ML Ranker
    participant Cassandra

    App->>Feed: GET /v1/feed
    Feed->>Redis: GET feed:ranked:{user_id}
    alt cache hit (< 5 min old)
        Redis-->>Feed: cached feed
    else cache miss
        Feed->>Graph: get friend list
        Graph->>TAO: get associations FRIENDS
        TAO-->>Graph: [friend_ids]
        Feed->>Cassandra: get recent posts from friends
        Feed->>Ranker: rank(posts, user_features)
        Ranker-->>Feed: ranked post_ids
        Feed->>Redis: SET feed:ranked:{user_id} TTL 300s
    end
    Feed-->>App: feed posts
```

---

## 5. Database Schema — Posts (Cassandra)

```sql
CREATE TABLE posts (
    post_id         UUID,
    author_id       BIGINT,
    content         TEXT,
    media_urls      LIST<TEXT>,
    visibility      INT,        -- PUBLIC=1, FRIENDS=2, CUSTOM=3
    created_at      TIMESTAMP,
    like_count      COUNTER,
    comment_count   INT,
    share_count     INT,
    PRIMARY KEY (author_id, created_at, post_id)
) WITH CLUSTERING ORDER BY (created_at DESC);

CREATE TABLE feed_candidates (
    user_id         BIGINT,
    post_id         UUID,
    author_id       BIGINT,
    score           FLOAT,
    created_at      TIMESTAMP,
    PRIMARY KEY (user_id, score, post_id)
) WITH CLUSTERING ORDER BY (score DESC);
```

---

## 6. Messenger Architecture

```mermaid
flowchart TB
    subgraph clients [Clients]
        C1[User A]
        C2[User B]
    end

    subgraph realtime [Real-Time Layer]
        LB[Sticky LB]
        WS1[Chat Server 1]
        WS2[Chat Server 2]
        PubSub[Redis Pub/Sub]
    end

    subgraph storage [Message Storage]
        HBase[(HBase - messages)]
        Redis2[(Redis - presence/typing)]
    end

    C1 <-->|WebSocket| LB --> WS1
    C2 <-->|WebSocket| LB --> WS2
    WS1 <--> PubSub
    WS2 <--> PubSub
    WS1 --> HBase
    WS2 --> HBase
    WS1 --> Redis2
```

**Message schema (HBase):**
```
Row key:  conversation_id + reversed_timestamp
Columns:  sender_id, content, type, read_status, media_url

Example row key: "conv_abc123\xFF\xFF\xFF\xFF\xFF\xFF\xFF\xFF"
(reversed timestamp for newest-first scan)
```

---

## 7. Sharding & Indexing Summary

| Component | Shard Key | Index Type |
|-----------|-----------|-----------|
| MySQL graph | `id1 (user_id)` | B-tree PK + secondary on id2 |
| TAO cache | `id1` | In-memory hash + LRU eviction |
| Cassandra posts | `author_id` | PK clustering by created_at |
| HBase messages | `conversation_id` | Row key prefix scan |
| Redis feed | `user_id` | Sorted set by ML score |
| Elasticsearch | `post_id` | Inverted index for search |

---

## 8. Fan-out Strategy

```mermaid
flowchart LR
    Post[New Post] --> Kafka
    Kafka --> Worker[Feed Worker]
    Worker --> Type{Author type?}
    Type -->|Regular user| Push[Push to follower feeds]
    Type -->|Page/Group| PushMembers[Push to members]
    Type -->|Celebrity 10M+| Skip[No fan-out]
    Push --> Redis[(Redis feed cache)]
    PushMembers --> Redis
```

---

## 9. Privacy Enforcement

```mermaid
flowchart TB
    Post[Post Created] --> Vis{visibility?}
    Vis -->|PUBLIC| All[All users]
    Vis -->|FRIENDS| Friends[Graph: friends of author]
    Vis -->|CUSTOM| Custom[Specific friend list]
    Feed[Feed Request] --> Check[Privacy Filter]
    Check --> All
    Check --> Friends
    Check --> Custom
    Check -->|not authorized| Block[Remove from feed]
```

---

## 10. Load Balancing

| Layer | Method | Purpose |
|-------|--------|---------|
| DNS | GeoDNS | Route to nearest data center |
| L7 ALB | Least connections | API + GraphQL traffic |
| Chat LB | IP hash (sticky) | WebSocket session persistence |
| TAO | Consistent hash on id1 | Cache locality |
| MySQL | Shard router on user_id | Database queries |

---

## 11. Interview Q&A

**Q: What is TAO and why not Redis?**  
A: TAO is graph-aware — stores associations (edges), not just key-value. One TAO call = "get all friends" vs multiple Redis calls. 99%+ cache hit rate, built for social graph access patterns.

**Q: How is feed different from Instagram?**  
A: Facebook feed is ML-ranked (not chronological). Candidate generation from friends + groups + pages. 1000+ ML features. Instagram is simpler chronological/ranked hybrid.

**Q: How suggest friends?**  
A: Offline Spark jobs nightly: mutual friends (Jaccard similarity), shared groups, contact import (hashed phone numbers), location proximity. ML model ranks candidates. Results cached in TAO.

**Q: How shard 500B graph edges?**  
A: MySQL sharded by id1 (source node). All edges from user X on same shard. Cross-shard queries use TAO scatter-gather with timeout.

**Q: Messenger vs WhatsApp?**  
A: Both use persistent connections. Facebook Messenger: WebSocket + HBase. WhatsApp: custom Erlang + RocksDB. Both guarantee at-least-once delivery with client-side dedup.

**Q: CAP for feed vs payments?**  
A: Feed/likes/notifications: AP. Ad billing/payments: CP with idempotency keys.

[← Back to index](../README.md)
