# Multiprocessing

## Files

| File | Description |
|------|-------------|
| `example.py` | `ProcessPoolExecutor`, `mp.Process`, and queue-based workers |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `square(n)` | Function | Simple map target for process pool |
| `cpu_heavy(n)` | Function | CPU-bound loop demo |
| `worker(queue, result_list)` | Function | Consumer process reading from a shared queue |

---

## What is multiprocessing?

The `multiprocessing` module spawns **separate processes**, each with its own Python interpreter and memory. Unlike threads, processes bypass the GIL for true CPU parallelism.

## Why interviewers ask

- Contrast with threading and async
- GIL explanation in practice
- When to use `ProcessPoolExecutor` vs `ThreadPoolExecutor`

## Key concepts

| Concept | Detail |
|---------|--------|
| `Process` | Independent process with separate memory |
| `Queue` / `Pipe` | IPC for passing data between processes |
| `ProcessPoolExecutor` | High-level pool for map/submit patterns |
| `if __name__ == "__main__"` | Required on Windows/macOS spawn to avoid recursive fork |

## Threading vs multiprocessing

| | Threading | Multiprocessing |
|---|-----------|-----------------|
| Memory | Shared | Separate |
| GIL | One bytecode thread at a time | Each process has own GIL |
| Best for | I/O-bound | CPU-bound |
| Overhead | Low | Higher (process spawn) |

## Common interview questions

1. **Why use multiprocessing over threading for number crunching?** — GIL prevents parallel CPU work in threads.
2. **Why guard with `if __name__ == "__main__"`?** — Prevents child processes re-importing and re-spawning infinitely.
3. **How do processes share data?** — Queues, Pipes, Manager, or shared memory — not plain global variables.

## Run

```bash
python3 example.py
```

## Related

- [threading](../threading/) — I/O-bound concurrency
- [async_await](../async_await/) — cooperative I/O
