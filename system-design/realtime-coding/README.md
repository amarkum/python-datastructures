# Real-Time Coding Platform — System Design (Detailed)

Complete system design for CoderPad/HackerRank Live — collaborative editor, WebSocket sync, OT/CRDT, Docker sandbox execution.

---

## 1. Requirements & Capacity

| Metric | Estimate |
|--------|----------|
| Concurrent sessions | 50,000 (peak) |
| WebSocket connections | 100,000 (2 per session) |
| Code runs/session | ~20 × 5s each |
| Peak code execution QPS | ~280/s |
| Edit sync latency target | < 100ms p99 |
| Languages supported | 10+ |

---

## 2. High-Level Architecture

```mermaid
flowchart TB
    subgraph clients [Browser Clients]
        Interviewer[Interviewer]
        Candidate[Candidate]
        Observer[Observer optional]
    end

    subgraph edge [Edge Layer]
        DNS[Route 53]
        LB[Sticky L7 LB - IP hash]
    end

    subgraph realtime [Real-Time Layer]
        WS1[WebSocket Server 1]
        WS2[WebSocket Server 2]
        WSN[WebSocket Server N]
        PubSub[Redis Pub/Sub]
    end

    subgraph backend [Backend Services]
        Session[Session Service]
        OT[OT/CRDT Engine]
        Exec[Code Execution Service]
        Pool[Container Pool Manager]
        Replay[Replay Service]
        Auth[Auth Service]
    end

    subgraph storage [Storage]
        Redis[(Redis - doc state/presence)]
        PG[(PostgreSQL - sessions/runs)]
        S3[(S3 - snapshots/replay)]
        Queue[SQS - exec queue]
    end

    Interviewer <-->|WSS| LB --> WS1
    Candidate <-->|WSS| LB --> WS2
    Observer <-->|WSS| LB --> WSN
    WS1 <--> PubSub
    WS2 <--> PubSub
    WSN <--> PubSub
    WS1 --> OT --> Redis
    Session --> PG
    Exec --> Queue --> Pool
    Pool --> Docker[Docker/gVisor Sandboxes]
    OT --> S3
    Replay --> S3
```

---

## 3. Sequence Diagrams

### 3.1 Session Creation

```mermaid
sequenceDiagram
    participant Interviewer
    participant API as Session Service
    participant PG as PostgreSQL
    participant Redis
    participant Email as Email Service

    Interviewer->>API: POST /v1/sessions { language: "python", title: "Interview" }
    API->>PG: INSERT session (status=ACTIVE)
    API->>Redis: SET doc:{session_id} { content: template, version: 0 }
    API->>Redis: SET session:{session_id}:meta { language, created_by, ... }
    API->>Email: send invite link to candidate
    API-->>Interviewer: { session_id, ws_url, editor_url, invite_token }
```

### 3.2 Real-Time Edit Sync (OT)

```mermaid
sequenceDiagram
    participant A as Interviewer (WS Server 1)
    participant OT as OT Engine
    participant PubSub as Redis Pub/Sub
    participant B as Candidate (WS Server 2)

    A->>OT: Op{ type:INSERT, pos:0, text:"def " }
    OT->>OT: apply locally, version=1
    OT->>Redis: SET doc:{id} content version=1
    OT->>PubSub: PUBLISH session:{id} { op, version:1, user:A }
    PubSub->>A: relay (echo back, ack)
    PubSub->>B: { op, version:1, user:A }
    B->>B: transform pending ops against version=1
    B->>B: apply transformed op locally

    Note over A,B: Both clients converge to same document state
```

### 3.3 Code Execution

```mermaid
sequenceDiagram
    participant Client
    participant Exec as Execution Service
    participant Queue as SQS Queue
    participant Pool as Container Pool
    participant Docker as Docker Sandbox
    participant WS as WebSocket Server

    Client->>Exec: POST /sessions/{id}/run { language, code }
    Exec->>Queue: enqueue job
    Exec-->>Client: 202 Accepted { run_id }
    Pool->>Queue: dequeue job
    Pool->>Docker: pull pre-warmed container
    Pool->>Docker: write code to /tmp/main.py
    Pool->>Docker: exec --network=none --memory=128m --timeout=5s python /tmp/main.py
    Docker-->>Pool: { stdout, stderr, exit_code, duration_ms }
    Pool->>Docker: destroy container
    Pool->>WS: push run_result to session channel
    WS-->>Client: { type: run_result, stdout, stderr, exit_code }
```

---

## 4. Database Schema (Detailed)

### 4.1 ER Diagram

```mermaid
erDiagram
    USERS ||--o{ SESSIONS : creates
    SESSIONS ||--o{ PARTICIPANTS : has
    SESSIONS ||--o{ CODE_RUNS : contains
    SESSIONS ||--o{ SNAPSHOTS : stores
    SESSIONS ||--o{ OP_LOG : tracks

    USERS {
        bigint user_id PK
        varchar email UK
        varchar name
        enum role
        timestamp created_at
    }

    SESSIONS {
        uuid session_id PK
        bigint created_by FK
        varchar title
        varchar language
        enum status
        timestamp started_at
        timestamp ended_at
        int duration_minutes
    }

    PARTICIPANTS {
        uuid session_id FK
        bigint user_id FK
        enum role
        timestamp joined_at
        timestamp left_at
    }

    CODE_RUNS {
        uuid run_id PK
        uuid session_id FK
        bigint triggered_by FK
        text code
        text stdout
        text stderr
        int exit_code
        int duration_ms
        timestamp created_at
    }

    SNAPSHOTS {
        uuid snapshot_id PK
        uuid session_id FK
        int version
        text content
        timestamp created_at
    }

    OP_LOG {
        uuid session_id FK
        int version
        jsonb operation
        bigint user_id
        timestamp created_at
    }
```

### 4.2 PostgreSQL DDL

```sql
CREATE TABLE sessions (
    session_id      UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_by      BIGINT NOT NULL REFERENCES users(user_id),
    title           VARCHAR(200),
    language        VARCHAR(30) NOT NULL DEFAULT 'python',
    template_code   TEXT,
    status          VARCHAR(20) NOT NULL DEFAULT 'active',
    started_at      TIMESTAMP DEFAULT NOW(),
    ended_at        TIMESTAMP,
    settings        JSONB DEFAULT '{}'
);

CREATE TABLE participants (
    session_id      UUID NOT NULL REFERENCES sessions(session_id),
    user_id         BIGINT NOT NULL REFERENCES users(user_id),
    role            VARCHAR(20) NOT NULL,  -- interviewer | candidate | observer
    joined_at       TIMESTAMP DEFAULT NOW(),
    left_at         TIMESTAMP,
    PRIMARY KEY (session_id, user_id)
);

CREATE TABLE code_runs (
    run_id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    session_id      UUID NOT NULL REFERENCES sessions(session_id),
    triggered_by    BIGINT NOT NULL,
    code            TEXT NOT NULL,
    language        VARCHAR(30) NOT NULL,
    stdout          TEXT,
    stderr          TEXT,
    exit_code       INT,
    duration_ms     INT,
    memory_used_kb  INT,
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE op_log (
    session_id      UUID NOT NULL,
    version         INT NOT NULL,
    operation       JSONB NOT NULL,
    user_id         BIGINT NOT NULL,
    created_at      TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (session_id, version)
);
```

### 4.3 Indexing Strategy

| Table | Index | Columns | Purpose |
|-------|-------|---------|---------|
| `sessions` | PK | `session_id` | Session lookup |
| `sessions` | `idx_sessions_user` | `(created_by, started_at DESC)` | User's past sessions |
| `sessions` | `idx_sessions_status` | `(status, started_at)` WHERE status='active' | Active sessions monitor |
| `code_runs` | `idx_runs_session` | `(session_id, created_at DESC)` | Run history per session |
| `op_log` | PK | `(session_id, version)` | Ordered op log for replay |
| `participants` | `idx_participants_user` | `(user_id, joined_at DESC)` | User participation history |

**Redis keys:**
| Key | Type | Purpose |
|-----|------|---------|
| `doc:{session_id}` | HASH | `{ content, version, language }` |
| `ops:{session_id}` | LIST | Recent ops buffer (last 1000) |
| `presence:{session_id}` | SET | Connected user_ids |
| `cursor:{session_id}:{user_id}` | STRING | `{ line, col }` cursor position |
| `pubsub:session:{session_id}` | CHANNEL | Real-time op broadcast |

---

## 5. Operational Transformation (OT) — Detailed

```mermaid
flowchart TB
    subgraph ot [OT Engine]
        Op1["Op A: INSERT 'hello' pos:0"]
        Op2["Op B: INSERT 'world' pos:0 (concurrent)"]
        Transform[Transform B against A]
        Result["B': INSERT 'world' pos:5"]
    end

    Op1 --> Transform
    Op2 --> Transform
    Transform --> Result

    Note["Final doc: 'helloworld' (both converge)"]
```

**OT operation types:**
```json
{ "type": "insert",  "pos": 5, "text": "hello" }
{ "type": "delete",  "pos": 3, "length": 2 }
{ "type": "retain",  "pos": 0, "length": 5 }
{ "type": "cursor",  "line": 10, "col": 3, "user_id": 1 }
```

**Transform rules (simplified):**
```
INSERT vs INSERT at same pos: later op shifts pos by text length
INSERT vs DELETE: adjust delete range if insert is before
DELETE vs DELETE: merge overlapping ranges
```

**Version tracking:**
```
Client sends: { op, client_version: 5, server_version: 4 }
Server: transform op against ops 4→5, apply, broadcast as version 6
Client: if client_version != server_version → fetch missing ops first
```

---

## 6. WebSocket Scaling

```mermaid
flowchart TB
    subgraph lb [Load Balancer]
        ALB[ALB - Sticky IP Hash]
    end

    subgraph ws_cluster [WebSocket Cluster]
        WS1[WS Server 1<br/>10K connections]
        WS2[WS Server 2<br/>10K connections]
        WS3[WS Server 3<br/>10K connections]
    end

    subgraph bridge [Cross-Server Bridge]
        PubSub[Redis Pub/Sub<br/>channel: session:id]
    end

    C1[Client A] --> ALB --> WS1
    C2[Client B] --> ALB --> WS2
    WS1 <--> PubSub
    WS2 <--> PubSub
    WS3 <--> PubSub
```

| Challenge | Solution |
|-----------|---------|
| Sticky sessions | ALB IP hash — same client → same WS server |
| Cross-server relay | Redis Pub/Sub per session channel |
| Connection limit | ~10K connections per WS server, scale horizontally |
| Reconnection | Client sends `{ resume_from_version: N }` on reconnect |
| Heartbeat | Ping/pong every 30s, disconnect after 3 missed |

---

## 7. Docker Sandbox — Security

```mermaid
flowchart TB
    subgraph pool [Container Pool Manager]
        Warm[Pre-warmed Pool<br/>python × 10<br/>javascript × 10<br/>java × 5]
    end

    subgraph sandbox [Sandbox Container]
        Code[User Code]
        Limits[Resource Limits]
        Isolation[Isolation]
    end

    Request[Run Request] --> pool
    pool --> sandbox
    Code --> Limits
    Limits --> Isolation
    Isolation --> Result[stdout/stderr/exit_code]
    Result --> Destroy[Destroy Container]
```

**Docker run command (full security):**
```bash
docker run \
  --rm \                          # destroy after run
  --network=none \                # no network access
  --memory=128m \                 # memory limit
  --memory-swap=128m \            # no swap escape
  --cpus=0.5 \                    # half CPU core
  --pids-limit=50 \               # prevent fork bomb
  --read-only \                   # read-only root FS
  --tmpfs /tmp:size=10M \         # writable temp only
  --user=1000:1000 \              # non-root user
  --security-opt=no-new-privileges \
  -v /code:/app:ro \              # code mounted read-only
  python:3.11-slim \
  timeout 5s python /app/main.py
```

| Threat | Mitigation |
|--------|-----------|
| Network exfiltration | `--network=none` |
| Crypto mining | No network + CPU limit |
| Fork bomb | `--pids-limit=50` |
| File system escape | Read-only root + gVisor |
| Infinite loop | `--timeout=5s` |
| Memory bomb | `--memory=128m` |
| Container escape | gVisor (user-space kernel) |

---

## 8. Sharding & Load Balancing

| Component | Strategy |
|-----------|----------|
| WebSocket servers | Horizontal scale, sticky LB |
| Redis doc state | Hash slot on session_id |
| PostgreSQL | session_id UUID (no shard needed at 50K concurrent) |
| S3 snapshots | Prefix `sessions/{session_id}/` |
| Execution workers | SQS queue — auto-scale workers by queue depth |
| Container pool | Per-language pools, pre-warm based on demand |

---

## 9. Replay System

```mermaid
flowchart LR
    Ops[Op Log in Redis] -->|every 30s| Snapshot[Full Snapshot to S3]
    Ops -->|on session end| Final[Final Snapshot]
    Final --> Replay[Replay Service]
    Snapshot --> Replay
    Replay --> Timeline[Timed Event Stream]
    Timeline --> UI[Replay UI]
```

**Replay API:**
```
GET /v1/sessions/{id}/replay
→ [
    { t: 0,    type: "snapshot", content: "def hello():..." },
    { t: 1500, type: "op", op: { insert, pos: 12, text: "world" }, user: "candidate" },
    { t: 3200, type: "run", stdout: "Hello world", exit_code: 0 },
    ...
  ]
```

---

## 10. API Design (Complete)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/v1/sessions` | Create session |
| GET | `/v1/sessions/{id}` | Session metadata |
| POST | `/v1/sessions/{id}/join` | Join with invite token |
| WS | `/v1/sessions/{id}/ws` | Real-time sync |
| POST | `/v1/sessions/{id}/run` | Execute code |
| GET | `/v1/sessions/{id}/runs` | Run history |
| GET | `/v1/sessions/{id}/replay` | Replay data |
| DELETE | `/v1/sessions/{id}` | End session |

**WebSocket message types:**
```json
{ "type": "op",       "op": {...}, "version": 42, "user_id": 1 }
{ "type": "cursor",   "line": 5, "col": 10, "user_id": 2 }
{ "type": "presence", "users": [{"id":1,"name":"Interviewer"},{"id":2,"name":"Candidate"}] }
{ "type": "run_result","run_id": "...", "stdout": "...", "stderr": "", "exit_code": 0 }
{ "type": "sync",     "content": "...", "version": 42 }
```

---

## 11. Interview Q&A

**Q: WebSocket vs HTTP polling?**  
A: WebSocket: full-duplex, ~1ms latency, 1 persistent connection. Polling: 1-5s delay, wastes bandwidth. Mandatory for live code sync.

**Q: OT vs CRDT?**  
A: OT: central server transforms ops (Google Docs model). CRDT: mathematically convergent, works P2P/offline (Figma, Apple Notes). OT simpler with central server — standard for interview platforms.

**Q: How sync across multiple WS servers?**  
A: Redis Pub/Sub channel per session. All WS servers subscribe. Op published once, all servers relay to their connected clients.

**Q: How run untrusted code?**  
A: Fresh Docker container per run. No network, CPU/memory/time limits, non-root, read-only FS, destroyed after. gVisor for extra isolation.

**Q: How handle 50K concurrent sessions?**  
A: 5-10 WS servers × 10K connections. Redis cluster for state. Execution workers auto-scale via SQS queue depth. Pre-warmed container pools per language.

**Q: What if client disconnects mid-edit?**  
A: On reconnect: send `{ resume_from_version: N }`. Server sends all ops from version N. Client replays ops locally to catch up.

**Q: How reduce code run cold start?**  
A: Pre-warm container pool (10 python, 10 node, 5 java containers always ready). Pull from pool on run, return to pool or destroy. Cold start: ~200ms vs ~2s.

[← Back to index](../README.md)
