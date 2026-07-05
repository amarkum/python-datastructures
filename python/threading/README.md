# Threading

## Files

| File | Description |
|------|-------------|
| `example.py` | Threads, locks, race conditions, and `ThreadPoolExecutor` |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `unsafe_increment()` | Function | Increments shared counter without a lock (race condition) |
| `safe_increment()` | Function | Same logic but protected by `threading.Lock` |
| `worker(name, delay)` | Function | Simple thread target for demos |
| `demonstrate_race_condition()` | Function | Shows unreliable counter without synchronization |
| `demonstrate_lock()` | Function | Shows correct counter with lock |

---

## What is threading in Python?

Threads share the same memory space within a process. Python's `threading` module is suited for **I/O-bound** tasks where threads wait on network, disk, or locks.

## Why interviewers ask

- Race conditions and locks are fundamental concurrency topics
- The **GIL** (Global Interpreter Lock) is one of the most asked Python questions
- Distinction between threading and multiprocessing

## The GIL (Global Interpreter Lock)

Only one thread executes Python bytecode at a time per process. This means threads don't give true CPU parallelism for compute-heavy work — use `multiprocessing` instead.

Threads still help when work is I/O-bound: a thread blocked on I/O releases the GIL.

## Key concepts

| Concept | Detail |
|---------|--------|
| `threading.Thread` | Spawn a new thread |
| `threading.Lock` | Mutual exclusion to prevent race conditions |
| `with lock:` | Acquire lock; auto-release on exit |
| `ThreadPoolExecutor` | Higher-level thread pool from `concurrent.futures` |
| Race condition | Unsynchronized access to shared mutable state |

## Common interview questions

1. **Why doesn't threading speed up CPU-bound Python code?** — The GIL.
2. **How do you prevent a race condition?** — Locks, queues, or immutable data.
3. **Thread vs process?** — Threads share memory; processes are isolated (safer for CPU work).

## Run

```bash
python3 example.py
```

## When to use what

- **I/O-bound, many connections** → `asyncio` or threading
- **CPU-bound** → `multiprocessing` or `ProcessPoolExecutor`
- **Simple parallel I/O** → `ThreadPoolExecutor`
