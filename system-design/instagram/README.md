# Instagram — System Design (Detailed)

Complete system design for a photo/video sharing platform at billion-user scale — feed fan-out, media CDN, Cassandra, Redis caching.

---

## 1. Requirements

| Functional | Non-Functional |
|------------|----------------|
| Upload photo/video + caption | Feed load < 500ms |
| Follow/unfollow users | 2B+ users, 100B+ posts |
| Home feed (chronological/ranked) | Read:write ratio 100:1 |
| Stories (24h expiry) | Global CDN for media |
| Like, comment, share | AP consistency for likes OK |
| Direct messages | 99.9% availability |
| Explore/discover page | Multi-region deployment |

---

## 2. Capacity Estimation

```
DAU = 500M
Posts/day = 100M (200M peak on events)
Feed reads/day = 50B (500 reads/user/day)
Peak feed QPS = 50B / 86400 × 3 (peak factor) ≈ 1.7M QPS

Media storage:
  100M posts × 2MB avg = 200TB/day × 365 = 73 PB/year
  Mitigation: CDN caches hot content, delete old resolutions

Metadata (Cassandra):
  100M posts × 500 bytes = 50GB/day × 365 = 18TB/year

Redis (feed cache):
  500M users × 500 post_ids × 8 bytes = 2TB feed cache
  Mitigation: only cache active users (30-day window) ≈ 600GB
```

---

## 3. High-Level Architecture

```mermaid
flowchart TB
    subgraph clients [Clients]
        iOS[iOS App]
        Android[Android App]
        Web[Web App]
    end

    subgraph edge [Edge Layer]
        CDN[CloudFront CDN - media]
        LB[L7 Load Balancer]
        GQL[GraphQL Gateway]
    end

    subgraph services [Microservices]
        Post[Post Service]
        Feed[Feed Service]
        User[User Service]
        Media[Media Processing]
        Story[Story Service]
        Social[Social Graph]
        Search[Search Service]
        Notify[Notification Service]
        Fanout[Fan-out Workers]
        Like[Like Service]
    end

    subgraph async [Async Processing]
        Kafka[Apache Kafka]
        Lambda[Lambda - image resize]
    end

    subgraph storage [Storage Layer]
        S3[(S3 - media blobs)]
        Cassandra[(Cassandra - posts/metadata)]
        Redis[(Redis Cluster - feeds/likes)]
        PG[(PostgreSQL - users/follows)]
        ES[(Elasticsearch - search/explore)]
    end

    iOS --> CDN
    Android --> CDN
    iOS --> LB
    Android --> LB
    Web --> LB
    LB --> GQL
    GQL --> Post
    GQL --> Feed
    GQL --> User
    GQL --> Story
    Post --> Media
    Media --> S3
    S3 --> Lambda
    Post --> Cassandra
    Post --> Kafka
    Kafka --> Fanout
    Fanout --> Redis
    Feed --> Redis
    Feed --> Cassandra
    Social --> PG
    Like --> Redis
    Search --> ES
    Kafka --> Notify
```

---

## 4. Sequence Diagrams

### 4.1 Photo Upload Flow

```mermaid
sequenceDiagram
    participant App as Mobile App
    participant Media as Media Service
    participant S3 as S3
    participant Lambda as Lambda/Worker
    participant Post as Post Service
    participant Cassandra as Cassandra
    participant Kafka as Kafka
    participant Fanout as Fan-out Worker
    participant Redis as Redis

    App->>Media: POST /v1/media/upload-request
    Media-->>App: { presigned_s3_url, media_id }
    App->>S3: PUT image directly (bypass API)
    S3->>Lambda: trigger on upload
    Lambda->>Lambda: resize thumbnail 150px, medium 640px, full 1080px
    Lambda->>S3: store all resolutions
    Lambda->>Post: POST /v1/posts { media_id, caption }
    Post->>Cassandra: INSERT post metadata
    Post->>Kafka: PostCreated event
    Kafka->>Fanout: consume event
    Fanout->>PG: get followers(user_id)
    loop for each follower (< 10K followers)
        Fanout->>Redis: ZADD feed:{follower_id} timestamp post_id
    end
```

### 4.2 Feed Read Flow

```mermaid
sequenceDiagram
    participant App as Mobile App
    participant Feed as Feed Service
    participant Redis as Redis Feed Cache
    participant Cassandra as Cassandra
    participant CDN as CDN

    App->>Feed: GET /v1/feed?cursor=&limit=20
    Feed->>Redis: ZREVRANGE feed:{user_id} 0 19
    Redis-->>Feed: [post_id_1, post_id_2, ...]
    Feed->>Feed: get celebrity post_ids (pull model)
    Feed->>Cassandra: BATCH GET post details (IN query)
    Cassandra-->>Feed: post objects
    Feed->>Feed: merge + deduplicate + rank
    Feed-->>App: { posts[], next_cursor }
    App->>CDN: GET thumbnail URLs (parallel)
```

---

## 5. Database Schema (Detailed)

### 5.1 ER Diagram

```mermaid
erDiagram
    USERS ||--o{ POSTS : creates
    USERS ||--o{ FOLLOWS : follows
    USERS ||--o{ STORIES : posts
    POSTS ||--o{ LIKES : receives
    POSTS ||--o{ COMMENTS : has
    POSTS ||--o{ MEDIA : contains

    USERS {
        bigint user_id PK
        varchar username UK
        varchar email UK
        varchar bio
        varchar profile_pic_url
        int follower_count
        int following_count
        timestamp created_at
    }

    POSTS {
        uuid post_id PK
        bigint user_id FK
        text caption
        timestamp created_at
        int like_count
        int comment_count
    }

    MEDIA {
        uuid media_id PK
        uuid post_id FK
        varchar type
        varchar thumbnail_url
        varchar medium_url
        varchar full_url
        int width
        int height
    }

    FOLLOWS {
        bigint follower_id PK
        bigint followee_id PK
        timestamp created_at
    }

    LIKES {
        uuid post_id PK
        bigint user_id PK
        timestamp created_at
    }

    COMMENTS {
        uuid comment_id PK
        uuid post_id FK
        bigint user_id FK
        text content
        timestamp created_at
    }
```

### 5.2 Cassandra Schema (Posts — Write-Heavy)

```sql
-- Partition by user_id, cluster by created_at DESC
-- Optimized for: "get all posts by user X, newest first"

CREATE TABLE posts_by_user (
    user_id         BIGINT,
    created_at      TIMESTAMP,
    post_id         UUID,
    caption         TEXT,
    media_ids       LIST<UUID>,
    like_count      COUNTER,
    comment_count   INT,
    PRIMARY KEY (user_id, created_at, post_id)
) WITH CLUSTERING ORDER BY (created_at DESC)
  AND compaction = {'class': 'TimeWindowCompactionStrategy'};

-- Lookup by post_id (for feed detail fetch)
CREATE TABLE posts_by_id (
    post_id         UUID PRIMARY KEY,
    user_id         BIGINT,
    caption         TEXT,
    media_ids       LIST<UUID>,
    like_count      INT,
    comment_count   INT,
    created_at      TIMESTAMP
);

-- Likes (high write volume)
CREATE TABLE likes_by_post (
    post_id         UUID,
    user_id         BIGINT,
    created_at      TIMESTAMP,
    PRIMARY KEY (post_id, user_id)
);
```

### 5.3 PostgreSQL Schema (Users & Social Graph)

```sql
CREATE TABLE users (
    user_id         BIGSERIAL PRIMARY KEY,
    username        VARCHAR(30) UNIQUE NOT NULL,
    email           VARCHAR(255) UNIQUE NOT NULL,
    password_hash   VARCHAR(255) NOT NULL,   -- bcrypt, NOT plain SHA
    bio             TEXT,
    profile_pic_url VARCHAR(500),
    follower_count  INT DEFAULT 0,
    following_count INT DEFAULT 0,
    is_private      BOOLEAN DEFAULT FALSE,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE follows (
    follower_id     BIGINT NOT NULL,
    followee_id     BIGINT NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (follower_id, followee_id)
);
```

### 5.4 Indexing Strategy

#### PostgreSQL Indexes

| Index | Columns | Type | Query Served |
|-------|---------|------|-------------|
| PK | `user_id` | B-tree | User lookup |
| `idx_users_username` | `username` | B-tree UNIQUE | Login, profile URL |
| `idx_users_email` | `email` | B-tree UNIQUE | Login |
| `idx_follows_followee` | `(followee_id, follower_id)` | B-tree composite | Fan-out worker: get all followers |
| `idx_follows_follower` | `(follower_id, followee_id)` | B-tree composite | "Who does user X follow?" |

**Critical fan-out index:**
```sql
-- Fan-out worker runs this for EVERY new post:
SELECT follower_id FROM follows WHERE followee_id = $author_id;
-- idx_follows_followee makes this O(log N) not full scan
```

#### Cassandra — No Manual Indexes Needed

Cassandra PRIMARY KEY **IS** the index:
```
PRIMARY KEY (user_id, created_at, post_id)
  → partition key: user_id (data co-located)
  → clustering key: created_at DESC (pre-sorted)
  → no secondary index needed for "posts by user"
```

**When to use Cassandra secondary index (avoid if possible):**
```sql
-- BAD: secondary index on post_id across all partitions
CREATE INDEX ON posts_by_user (post_id);  -- scatter-gather, slow

-- GOOD: denormalize into posts_by_id table (write twice, read fast)
INSERT INTO posts_by_user ...;
INSERT INTO posts_by_id ...;
```

#### Redis — Feed Index

```
Key:   feed:{user_id}
Type:  Sorted Set (ZSET)
Score: post created_at timestamp (unix ms)
Member: post_id (UUID string)

Commands:
  ZADD feed:12345 1700000000000 "post-uuid-1"   ← fan-out write
  ZREVRANGE feed:12345 0 19                      ← feed read (top 20)
  ZREMRANGEBYRANK feed:12345 0 -1001             ← trim to 1000 posts max
  ZCARD feed:12345                               ← feed size
```

#### Elasticsearch — Explore/Search Index

```json
{
  "mappings": {
    "posts": {
      "properties": {
        "post_id":       { "type": "keyword" },
        "user_id":       { "type": "long" },
        "caption":       { "type": "text", "analyzer": "standard" },
        "hashtags":      { "type": "keyword" },
        "like_count":    { "type": "integer" },
        "created_at":    { "type": "date" },
        "engagement_score": { "type": "float" }
      }
    }
  }
}
```

---

## 6. Feed Fan-out — Detailed

```mermaid
flowchart TB
    subgraph write [Write Path - on new post]
        Post[New Post] --> Kafka
        Kafka --> Worker[Fan-out Worker]
        Worker --> Check{follower count?}
        Check -->|< 10K followers| Push[Push to all follower feeds]
        Check -->|> 10K followers| Skip[Skip fan-out - celebrity]
        Push --> Redis[(Redis ZADD feed:follower_id)]
    end

    subgraph read [Read Path - on feed request]
        User[User opens app] --> FeedSvc[Feed Service]
        FeedSvc --> RedisRead[ZREVRANGE feed:user_id]
        FeedSvc --> CelebPull[Fetch celebrity posts]
        RedisRead --> Merge[Merge + deduplicate]
        CelebPull --> Merge
        Merge --> Cassandra[BATCH GET post details]
        Cassandra --> Response[Return feed]
    end
```

| User Type | Followers | Write Strategy | Read Strategy |
|-----------|-----------|---------------|---------------|
| Normal user | < 10K | Push to all follower Redis feeds | Read pre-built Redis feed |
| Power user | 10K – 1M | Push (async, may lag seconds) | Read Redis + merge |
| Celebrity | > 1M | **No fan-out** (would write 50M Redis keys) | Pull at read time |

**Celebrity pull at read:**
```python
def get_feed(user_id):
    post_ids = redis.zrevrange(f"feed:{user_id}", 0, 19)
    celebrity_ids = get_celebrity_follows(user_id)
    for celeb_id in celebrity_ids:
        recent = cassandra.get_recent_posts(celeb_id, limit=5)
        post_ids = merge(post_ids, recent)
    return fetch_post_details(post_ids)
```

---

## 7. Sharding Strategy

```mermaid
flowchart TB
    subgraph cassandra [Cassandra Cluster]
        N1[Node 1<br/>token range 0-25%]
        N2[Node 2<br/>token range 25-50%]
        N3[Node 3<br/>token range 50-75%]
        N4[Node 4<br/>token range 75-100%]
    end

    subgraph pg [PostgreSQL Shards]
        PG1[(Shard 1<br/>user_id 0-500M)]
        PG2[(Shard 2<br/>user_id 500M-1B)]
    end

    Post[Post Service] -->|user_id partition key| cassandra
    User[User Service] -->|user_id hash| pg
```

| Store | Shard Key | Strategy |
|-------|-----------|----------|
| Cassandra posts | `user_id` | Partition key — all user posts on same node |
| PostgreSQL users | `user_id % 2` | Hash sharding across 2+ shards |
| Redis feeds | `user_id` | Redis Cluster hash slot |
| S3 media | `user_id/post_id` | Prefix sharding — no hot partitions |
| Kafka | `user_id` | Partition — ordered events per user |

---

## 8. Media Pipeline

```mermaid
flowchart LR
    Upload[Client Upload] --> S3Raw[S3 raw/ bucket]
    S3Raw --> Lambda[Lambda Trigger]
    Lambda --> Thumb[thumbnail 150x150]
    Lambda --> Med[medium 640px]
    Lambda --> Full[full 1080px]
    Lambda --> Video[video: HLS transcode]
    Thumb --> S3Out[S3 media/ bucket]
    Med --> S3Out
    Full --> S3Out
    Video --> S3Out
    S3Out --> CDN[CloudFront CDN]
    CDN --> Client[Client displays]
```

| Resolution | Size | Use Case |
|-----------|------|----------|
| thumbnail | 150×150 | Feed grid, profile grid |
| medium | 640px wide | Feed scroll view |
| full | 1080px wide | Full-screen view |
| HLS video | 360p/720p/1080p | Video posts, Stories |

---

## 9. Load Balancing & CDN

```mermaid
flowchart TB
    User[User in Tokyo] --> DNS[GeoDNS]
    DNS --> CDN[CloudFront PoP Tokyo]
    CDN -->|cache HIT| User
    CDN -->|cache MISS| Origin[S3 Origin US]
    User -->|API calls| ALB[ALB - nearest region]
    ALB --> FeedSvc[Feed Service pods]
```

**CDN cache policy:**
```
/media/{post_id}/thumbnail  → Cache 30 days (immutable URL)
/media/{post_id}/full       → Cache 7 days
/v1/feed                    → NO CACHE (personalized)
/v1/users/{id}              → Cache 5 min (public profiles)
```

---

## 10. Like System at Scale

```mermaid
sequenceDiagram
    participant App
    participant Like as Like Service
    participant Redis
    participant Kafka
    participant Worker as Flush Worker
    participant Cassandra

    App->>Like: POST /v1/posts/{id}/like
    Like->>Redis: INCR post:likes:{post_id}
    Like->>Redis: SADD post:likers:{post_id} user_id
    Like-->>App: 200 OK (immediate)
    Like->>Kafka: LikeEvent (async)
    Worker->>Kafka: consume batch
    Worker->>Cassandra: UPDATE like_count (batch)
```

**Why not write Cassandra on every like?**
- 1B likes/day = 11,574 writes/sec to Cassandra
- Redis INCR = 100K+ ops/sec per node
- Batch flush every 30 seconds = 99% reduction in Cassandra writes

---

## 11. Interview Q&A

**Q: Push vs pull fan-out?**  
A: Push: write post_id to follower feeds on post (fast reads). Pull: fetch at read time (for celebrities with millions of followers). Hybrid is industry standard.

**Q: Why Cassandra for posts?**  
A: Write-heavy, time-ordered access pattern, horizontal scale. Partition by user_id = all posts co-located. No joins needed.

**Q: Why not store images in DB?**  
A: DB not designed for blobs. S3 + CDN = cheaper, faster, globally distributed. DB stores URLs only.

**Q: How index feed for fast reads?**  
A: Redis Sorted Set — score=timestamp, member=post_id. O(log N + 20) for top 20 posts. Pre-computed on write.

**Q: How handle 1M QPS feed reads?**  
A: Redis cluster (100K ops/node × 20 nodes). Feed pre-computed. CDN for media. Stateless Feed Service pods auto-scale.

**Q: Consistency model?**  
A: AP for likes (eventual, OK if count off by few). CP for post creation (must not lose posts). Feed may lag 1-2s behind post.

[← Back to index](../README.md)
