# Async / Await

Cooperative concurrency for I/O-bound work — single thread, event loop, no thread overhead.

## Files

| File | Description |
|------|-------------|
| `example.py` | Coroutines, `gather`, `create_task`, async generator |

---

## Descriptive Example

### Scenario

Fetch data from three "APIs" concurrently — total time ≈ slowest call, not sum of all calls.

```python
import asyncio

async def fetch(name, delay):
    print(f"  [{name}] starting")
    await asyncio.sleep(delay)      # simulates I/O wait
    print(f"  [{name}] done")
    return f"result-{name}"

async def main():
    results = await asyncio.gather(
        fetch("A", 0.2),
        fetch("B", 0.1),
        fetch("C", 0.15),
    )
    print(results)

asyncio.run(main())
# All three start nearly together; total ~0.2s not 0.45s
```

### Calling async correctly

```python
coro = fetch("X", 0.1)
print(coro)             # <coroutine object> — NOT executed yet!
result = await coro     # inside async function
# or
asyncio.run(fetch("X", 0.1))   # from sync code
```

---

## Interview Q&A

**Q1: What is a coroutine?**  
A: Function defined with `async def`. Calling it returns a coroutine object — it doesn't run until awaited or passed to the event loop.

**Q2: When should you NOT use async?**  
A: CPU-bound tasks. Async won't parallelize computation. Use multiprocessing or run CPU work in `loop.run_in_executor()`.

**Q3: `asyncio.gather` vs `create_task`?**  
A: `create_task` schedules immediately and returns a Task. `gather` waits for multiple coroutines/tasks and returns all results (or raises first exception).

**Q4: Async vs threading?**  
A: Async: single thread, cooperative, no GIL contention, lower overhead. Threading: preemptive, good for blocking libraries that can't be made async.

**Q5: What is the event loop?**  
A: Schedules and runs coroutines. When a coroutine hits `await`, control returns to the loop to run other ready coroutines.

**Q6: What frameworks use async Python?**  
A: FastAPI, aiohttp, Starlette, asyncio-based DB drivers. Django 3.1+ has async views; full async ORM support varies.

---

## Run

```bash
python3 example.py
```
