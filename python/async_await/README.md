# Async / Await

## Files

| File | Description |
|------|-------------|
| `example.py` | Coroutines, `gather`, `create_task`, and async generators |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `fetch_data(name, delay)` | Coroutine | Simulates async I/O with `asyncio.sleep` |
| `gather_example()` | Coroutine | Runs multiple coroutines concurrently via `gather` |
| `task_example()` | Coroutine | Schedules work with `asyncio.create_task` |
| `async_generator()` | Async generator | Yields values with `async for` |
| `main()` | Coroutine | Entry point orchestrating all demos |

---

## What is async Python?

`async def` defines a **coroutine** — a function that can pause with `await` and resume later. `asyncio` runs coroutines on a single thread using an event loop, ideal for I/O-bound work (network, disk).

## Why interviewers ask

- Modern web backends (FastAPI, aiohttp) are async-heavy
- Tests understanding of concurrency vs parallelism
- Common confusion: async is not multithreading

## Key concepts

| Concept | Detail |
|---------|--------|
| `async def` | Defines a coroutine function |
| `await` | Pauses until the awaited coroutine/task completes |
| `asyncio.run()` | Entry point to run the event loop |
| `asyncio.gather()` | Run multiple coroutines concurrently |
| `asyncio.create_task()` | Schedule a coroutine as a Task |
| `async for` / `async with` | Async iteration and context managers |

## Async vs threading vs multiprocessing

| Model | Best for | GIL impact |
|-------|----------|------------|
| **asyncio** | Many I/O waits (API calls) | Single thread, cooperative |
| **threading** | I/O-bound with blocking libs | GIL limits CPU parallelism |
| **multiprocessing** | CPU-bound work | Separate processes, no shared GIL |

## Common interview questions

1. **When should you NOT use async?** — CPU-bound tasks; use multiprocessing instead.
2. **What happens if you call an async function without `await`?** — You get a coroutine object; it doesn't run.
3. **Difference between `gather` and `create_task`?** — Tasks start immediately; `gather` waits for all to finish.

## Run

```bash
python3 example.py
```
