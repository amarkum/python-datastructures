# System Design

Interview-focused system design — **one folder per product**, each with full architecture, data models, APIs, scaling, and Q&A.

## Companies & Products

| Folder | Product | Key challenge |
|--------|---------|---------------|
| [uber/](./uber/) | Uber | Real-time driver matching, geospatial indexing |
| [instagram/](./instagram/) | Instagram | Feed fan-out, media CDN, billion-scale likes |
| [facebook/](./facebook/) | Facebook | Social graph (TAO), ML feed ranking |
| [airbnb/](./airbnb/) | Airbnb | Geo search, booking consistency, payments |
| [url-shortener/](./url-shortener/) | bit.ly / TinyURL | Base62 encoding, redirect at scale |
| [realtime-coding/](./realtime-coding/) | CoderPad / HackerRank Live | WebSocket sync, code sandbox |

## Core Building Blocks (used across all designs)

| Concept | Used for |
|---------|----------|
| **Load Balancing** | Distribute traffic — L4/L7, round robin, sticky sessions (WebSocket) |
| **Sharding** | Partition DB by `user_id`, `city_id`, geohash |
| **Indexing** | B-tree, composite, geospatial (Uber/Airbnb), inverted (search) |
| **Databases** | SQL (ACID: trips, bookings) · NoSQL (feeds, URLs, locations) |
| **Caching** | Redis — feeds, GPS, URL mappings, availability calendars |
| **API Design** | REST + GraphQL + WebSocket; pagination, rate limits, idempotency |
| **Hashing** | SHA-256 (passwords), Base62 (URL codes), consistent hashing (shards) |
| **Encryption** | TLS in-transit, AES at-rest, PCI for payments |
| **CDN** | Photos, videos, static assets (Instagram, Facebook, Airbnb) |
| **Message Queues** | Kafka — async fan-out, analytics, notifications |
| **CAP Theorem** | CP for bookings/payments · AP for feeds/likes |

## How to approach any interview

```
1. Clarify requirements  →  functional + scale (DAU, QPS, read/write ratio)
2. Estimate capacity     →  storage, bandwidth, servers
3. High-level diagram    →  Client → CDN → LB → Services → DB/Cache/Queue
4. Data model + APIs     →  entities, endpoints
5. Deep dive             →  bottlenecks, sharding, caching
6. Trade-offs            →  CAP, SQL vs NoSQL, push vs pull
```

## Scale guide

| DAU | Stack |
|-----|-------|
| 1M | Monolith + read replicas + Redis |
| 10M | Microservices + sharding + CDN + Kafka |
| 100M+ | Multi-region + eventual consistency |

## Quick comparison

| Concept | Uber | Instagram | Facebook | Airbnb | URL Shortener | Real-Time Coding |
|---------|------|-----------|----------|--------|---------------|------------------|
| Load Balancer | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ sticky WS |
| Sharding | city_id | user_id | user_id | region | hash(code) | session_id |
| Cache | Redis GPS | Redis feed | TAO + Redis | Redis cal | Redis URLs | Redis doc |
| Queue | Kafka | Kafka | Kafka | Kafka | Kafka | Redis Pub/Sub |
| SQL | PostgreSQL | PostgreSQL | MySQL | PostgreSQL | — | PostgreSQL |
| NoSQL | Redis | Cassandra | Cassandra | Elasticsearch | DynamoDB | Redis |

Open any folder above for the **full detailed design**.
