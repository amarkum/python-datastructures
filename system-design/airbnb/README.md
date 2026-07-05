# Airbnb — System Design (Detailed)

Complete system design for a short-term rental marketplace — Elasticsearch geo search, booking consistency, payment escrow, reviews.

---

## 1. Requirements & Capacity

| Metric | Estimate |
|--------|----------|
| Active listings | 7M |
| Searches/day | 500M |
| Bookings/day | 1M |
| Peak search QPS | ~10,000/s |
| Listing photos | 7M × 20 × 1MB ≈ 140 TB |
| Booking records/year | 365M × 1KB ≈ 365 GB |

---

## 2. High-Level Architecture

```mermaid
flowchart TB
    subgraph clients [Clients]
        Guest[Guest App/Web]
        Host[Host App/Web]
    end

    subgraph edge [Edge]
        CDN[CloudFront - listing photos]
        LB[L7 ALB]
        GW[API Gateway]
    end

    subgraph services [Microservices]
        Search[Search Service]
        List[Listing Service]
        Book[Booking Service]
        Cal[Calendar Service]
        Pay[Payment Service]
        Review[Review Service]
        Msg[Messaging Service]
        Host[Host Management]
        Notify[Notification Service]
    end

    subgraph async [Async]
        Kafka[Kafka]
        CDC[CDC Connector]
    end

    subgraph storage [Storage]
        ES[(Elasticsearch Cluster)]
        PG[(PostgreSQL Primary)]
        PGReplica[(PostgreSQL Replicas)]
        Redis[(Redis Cluster)]
        S3[(S3 - photos)]
    end

    subgraph external [External]
        Stripe[Stripe Connect]
        Maps[Google Maps]
    end

    Guest --> CDN
    Guest --> LB --> GW
    Host --> LB
    GW --> Search --> ES
    GW --> Search --> Redis
    GW --> Book --> PG
    GW --> List --> S3
    Book --> Redis
    Cal --> PG
    Book --> Kafka
    PG --> CDC --> Kafka --> ES
    Kafka --> Pay --> Stripe
    Kafka --> Notify
    PG --> PGReplica
```

---

## 3. Sequence Diagrams

### 3.1 Search Flow

```mermaid
sequenceDiagram
    participant Guest
    participant Search as Search Service
    participant Redis
    participant ES as Elasticsearch
    participant CDN

    Guest->>Search: GET /search?lat=48.85&lng=2.35&check_in=Jul-01&check_out=Jul-05&guests=2
    Search->>Redis: GET cache:search:paris:2026-07-01:2guests
    alt cache hit
        Redis-->>Search: cached results
    else cache miss
        Search->>ES: geo + filter query
        ES-->>Search: ranked listing_ids
        Search->>Redis: SET cache TTL 5min
    end
        Search-->>Guest: { listings[], total, facets }
    Guest->>CDN: GET listing photos (parallel)
```

### 3.2 Booking Flow (CP — Strong Consistency)

```mermaid
sequenceDiagram
    participant Guest
    participant Book as Booking Service
    participant PG as PostgreSQL
    participant Redis
    participant Kafka
    participant Pay as Payment Service
    participant Stripe

    Guest->>Book: POST /bookings {listing_id, check_in, check_out, guests}
    Book->>PG: BEGIN TRANSACTION
    Book->>PG: SELECT availability FOR UPDATE (row lock)
    PG-->>Book: dates available ✓
    Book->>PG: INSERT booking CONFIRMED
    Book->>PG: UPDATE availability SET status=booked
    Book->>PG: COMMIT
    Book->>Redis: INVALIDATE cache:listing:{id}:availability
    Book->>Kafka: BookingConfirmed event
    Book-->>Guest: { booking_id, total_price }
    Kafka->>Pay: consume event
    Pay->>Stripe: charge(idempotency_key, amount)
    Stripe-->>Pay: payment_intent_id
    Pay->>PG: INSERT payment SUCCESS
```

---

## 4. Database Schema (Detailed)

### 4.1 ER Diagram

```mermaid
erDiagram
    USERS ||--o{ LISTINGS : hosts
    USERS ||--o{ BOOKINGS : makes
    LISTINGS ||--o{ BOOKINGS : receives
    LISTINGS ||--o{ AVAILABILITY : has
    LISTINGS ||--o{ LISTING_PHOTOS : has
    LISTINGS ||--o{ REVIEWS : receives
    BOOKINGS ||--|| PAYMENTS : has
    BOOKINGS ||--o{ REVIEWS : generates

    USERS {
        bigint user_id PK
        varchar email UK
        varchar name
        enum role
        varchar stripe_account_id
        timestamp created_at
    }

    LISTINGS {
        bigint listing_id PK
        bigint host_id FK
        varchar title
        text description
        decimal lat
        decimal lng
        decimal price_per_night
        int max_guests
        int bedrooms
        jsonb amenities
        decimal rating_avg
        int review_count
        enum status
    }

    AVAILABILITY {
        bigint listing_id PK
        date date PK
        enum status
        uuid booking_id FK
        int version
    }

    BOOKINGS {
        uuid booking_id PK
        bigint listing_id FK
        bigint guest_id FK
        date check_in
        date check_out
        int guests
        decimal total_price
        decimal service_fee
        enum status
        varchar idempotency_key UK
        timestamp created_at
    }

    PAYMENTS {
        uuid payment_id PK
        uuid booking_id FK UK
        decimal amount
        enum status
        varchar stripe_intent_id UK
        timestamp created_at
    }

    REVIEWS {
        uuid review_id PK
        uuid booking_id FK
        bigint reviewer_id
        bigint reviewee_id
        int score
        text comment
        enum type
        timestamp created_at
    }
```

### 4.2 PostgreSQL DDL

```sql
CREATE TABLE listings (
    listing_id      BIGSERIAL PRIMARY KEY,
    host_id         BIGINT NOT NULL REFERENCES users(user_id),
    title           VARCHAR(200) NOT NULL,
    description     TEXT,
    lat             DECIMAL(10, 8) NOT NULL,
    lng             DECIMAL(11, 8) NOT NULL,
    price_per_night DECIMAL(10, 2) NOT NULL,
    max_guests      INT NOT NULL DEFAULT 2,
    bedrooms        INT,
    bathrooms       INT,
    amenities       JSONB DEFAULT '[]',
    house_rules     JSONB DEFAULT '[]',
    rating_avg      DECIMAL(3, 2) DEFAULT 0,
    review_count    INT DEFAULT 0,
    status          VARCHAR(20) DEFAULT 'active',
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE availability (
    listing_id      BIGINT NOT NULL,
    date            DATE NOT NULL,
    status          VARCHAR(20) NOT NULL DEFAULT 'available',
    booking_id      UUID,
    version         INT NOT NULL DEFAULT 0,
    PRIMARY KEY (listing_id, date)
);

CREATE TABLE bookings (
    booking_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    listing_id      BIGINT NOT NULL REFERENCES listings(listing_id),
    guest_id        BIGINT NOT NULL REFERENCES users(user_id),
    check_in        DATE NOT NULL,
    check_out       DATE NOT NULL,
    guests          INT NOT NULL,
    total_price     DECIMAL(10, 2) NOT NULL,
    service_fee     DECIMAL(10, 2),
    host_payout     DECIMAL(10, 2),
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
    idempotency_key VARCHAR(100) UNIQUE NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW(),
    confirmed_at    TIMESTAMP,
    cancelled_at    TIMESTAMP
);
```

### 4.3 Indexing Strategy — PostgreSQL

| Index | Columns | Type | Purpose |
|-------|---------|------|---------|
| PK | `listing_id` | B-tree | Primary lookup |
| `idx_listings_host` | `(host_id, status)` | B-tree composite | Host dashboard: my listings |
| `idx_listings_location` | `(lat, lng)` | GiST (PostGIS) | Fallback geo query |
| `idx_listings_rating` | `(rating_avg DESC)` | B-tree | Sort by rating |
| `idx_availability_listing_date` | `(listing_id, date, status)` | B-tree composite | Booking availability check |
| `idx_bookings_guest` | `(guest_id, created_at DESC)` | B-tree composite | Guest trip history |
| `idx_bookings_listing` | `(listing_id, check_in)` | B-tree composite | Host calendar view |
| `idx_bookings_idempotency` | `(idempotency_key)` | B-tree UNIQUE | Prevent duplicate bookings |
| `idx_reviews_listing` | `(listing_id, created_at DESC)` | B-tree composite | Listing reviews page |

**Critical booking index:**
```sql
-- This query runs inside a transaction with FOR UPDATE:
SELECT date, status, version FROM availability
WHERE listing_id = $1
  AND date BETWEEN $2 AND $3
FOR UPDATE;

-- idx_availability_listing_date makes this O(log N + days)
-- NOT a full table scan
```

**GiST index for PostGIS (backup geo search):**
```sql
CREATE INDEX idx_listings_geo ON listings
USING GIST (ST_MakePoint(lng, lat));
-- Used when Elasticsearch is down (fallback)
```

---

## 5. Elasticsearch Index Design

```json
{
  "settings": {
    "number_of_shards": 5,
    "number_of_replicas": 2,
    "analysis": {
      "analyzer": {
        "listing_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "stemmer"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "listing_id":    { "type": "long" },
      "title":         { "type": "text", "analyzer": "listing_analyzer" },
      "description":   { "type": "text", "analyzer": "listing_analyzer" },
      "location":      { "type": "geo_point" },
      "price":         { "type": "float" },
      "rating":        { "type": "float" },
      "review_count":  { "type": "integer" },
      "max_guests":    { "type": "integer" },
      "bedrooms":      { "type": "integer" },
      "amenities":     { "type": "keyword" },
      "property_type": { "type": "keyword" },
      "blocked_dates": { "type": "date", "format": "yyyy-MM-dd" },
      "instant_book":  { "type": "boolean" },
      "superhost":     { "type": "boolean" },
      "photo_url":     { "type": "keyword", "index": false }
    }
  }
}
```

**Search query example:**
```json
{
  "query": {
    "bool": {
      "filter": [
        { "geo_distance": {
            "distance": "20km",
            "location": { "lat": 48.8566, "lon": 2.3522 }
        }},
        { "range": { "price": { "lte": 200 } } },
        { "term": { "max_guests": { "gte": 2 } } },
        { "terms": { "amenities": ["wifi", "kitchen"] } },
        { "bool": { "must_not": {
            "terms": { "blocked_dates": ["2026-07-01","2026-07-02","2026-07-03","2026-07-04"] }
        }}}
      ],
      "should": [
        { "rank_feature": { "field": "rating" } },
        { "term": { "superhost": { "value": true, "boost": 1.5 } } }
      ]
    }
  },
  "sort": [{ "_score": "desc" }, { "price": "asc" }],
  "from": 0, "size": 20
}
```

### 5.1 Elasticsearch Indexing & Sharding

```mermaid
flowchart LR
    PG[(PostgreSQL)] -->|CDC Debezium| Kafka
    Kafka --> ESWorker[ES Index Worker]
    ESWorker --> ES1[ES Shard 1<br/>listing_id 0-1.4M]
    ESWorker --> ES2[ES Shard 2<br/>listing_id 1.4M-2.8M]
    ESWorker --> ES3[ES Shard 3<br/>...]
```

| ES Concept | Configuration | Reason |
|-----------|--------------|--------|
| Shards | 5 primary | 7M docs / 5 = 1.4M per shard (optimal) |
| Replicas | 2 | High search QPS, fault tolerance |
| Refresh interval | 5s | Near real-time availability updates |
| Field: location | geo_point | Native geo_distance queries |
| Field: blocked_dates | date array | Filter unavailable dates in query |

---

## 6. Sharding Strategy

```mermaid
flowchart TB
    subgraph pg [PostgreSQL]
        Primary[(Primary - writes)]
        R1[(Replica 1 - reads)]
        R2[(Replica 2 - reads)]
    end

    subgraph es [Elasticsearch]
        ES1[Shard 1]
        ES2[Shard 2]
        ES3[Shard 3]
    end

    Book[Booking Service] -->|writes| Primary
    Search[Search Service] -->|reads| R1
    Search -->|reads| R2
    Search --> ES1
    Search --> ES2
    Primary -->|CDC| ES1
```

| Data | Sharding | Reason |
|------|----------|--------|
| Listings | ES hash routing | Even search distribution |
| Bookings | PostgreSQL (single primary + replicas) | Strong consistency needed |
| Availability | Co-located with listing_id | Same shard as listing |
| Photos | S3 prefix `listings/{listing_id}/` | No hot partitions |
| Search cache | Redis hash slot by query hash | Popular city queries cached |

---

## 7. Payment Escrow Flow

```mermaid
stateDiagram-v2
    [*] --> ChargeGuest : Booking confirmed
    ChargeGuest --> FundsHeld : Stripe charge success
    FundsHeld --> ReleasedToHost : Check-in day
    FundsHeld --> RefundedToGuest : Cancellation
    ReleasedToHost --> [*]
    RefundedToGuest --> [*]
```

**Stripe Connect flow:**
```
1. Guest charged $500 (total) on booking
2. $500 held in Airbnb Stripe platform account
3. Check-in day: transfer $420 to host Stripe Connect account
4. $80 retained as Airbnb service fee (14% + guest fee)
5. Cancellation: refund per policy (flexible/moderate/strict)
```

---

## 8. Load Balancing & Caching

```mermaid
flowchart TB
    User[User] --> DNS[Route 53]
    DNS --> ALB[ALB - L7]
    ALB --> Search1[Search Pod 1]
    ALB --> Search2[Search Pod 2]
    ALB --> Book1[Booking Pod 1]
    Search1 --> Redis[(Redis - search cache)]
    Search1 --> ES[(Elasticsearch)]
    Book1 --> PG[(PostgreSQL Primary)]
```

| Cache Key | TTL | Invalidation |
|-----------|-----|-------------|
| `search:{city}:{dates}:{guests}` | 5 min | On new booking in city |
| `listing:{id}:detail` | 10 min | On listing update |
| `listing:{id}:availability:{month}` | 2 min | On booking/cancellation |
| `host:{id}:dashboard` | 5 min | On new booking |

---

## 9. Interview Q&A

**Q: Why Elasticsearch over PostgreSQL for search?**  
A: Native geo_distance queries, full-text with scoring, faceted filters (amenities, price range), handles 10K QPS search. PostGIS works but doesn't scale as well for complex ranked search.

**Q: How prevent double-booking?**  
A: `SELECT FOR UPDATE` row lock inside PostgreSQL transaction. Only one booking transaction can lock overlapping dates. Return HTTP 409 if conflict.

**Q: How sync availability to Elasticsearch?**  
A: CDC (Change Data Capture) via Debezium — PostgreSQL WAL → Kafka → ES index worker updates `blocked_dates` field. Near real-time (5s lag).

**Q: Optimistic vs pessimistic locking?**  
A: Pessimistic (`FOR UPDATE`) for booking — simpler, guarantees no conflict. Optimistic (version column) for listing edits — higher concurrency, retry on conflict.

**Q: CP or AP?**  
A: CP for bookings and payments. AP acceptable for search results (5-min cache staleness OK) and review counts.

**Q: How handle holiday search spikes?**  
A: Redis cache for top 100 city+date combos. ES read replicas auto-scale. CDN for photos. Booking service rate-limited separately from search.

[← Back to index](../README.md)
