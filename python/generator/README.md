# Generators

## Files

| File | Description |
|------|-------------|
| `example.py` | Generator functions, expressions, and `.send()` demo |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `countdown(n)` | Generator | Yields numbers from n down to 1 |
| `fibonacci(limit)` | Generator | Yields Fibonacci numbers below a limit |
| `read_large_file_lines(path)` | Generator | Memory-efficient line-by-line file reading |
| `send_example()` | Generator | Demonstrates two-way communication via `.send()` |

---

## What is a generator?

A function that uses `yield` instead of `return`. Each `yield` pauses execution and returns a value; the next call resumes where it left off. Generators are **lazy** — they produce values on demand.

## Why interviewers ask

- Memory efficiency for large datasets
- Understanding the difference between eager and lazy evaluation
- Pipeline patterns in data processing

## Key concepts

| Concept | Detail |
|---------|--------|
| `yield` | Pauses function, returns value to caller |
| `next()` | Advance generator; raises `StopIteration` when done |
| `.send(value)` | Send a value into the generator at the current `yield` |
| Generator expression | `(x for x in items)` — like list comp but lazy |
| `yield from` | Delegate to another generator/sub-iterator |

## Generator vs list comprehension

```python
[x * 2 for x in range(10**6)]   # builds full list in memory
(x * 2 for x in range(10**6))   # yields one at a time
```

## Common interview questions

1. **Why use a generator to read a 10 GB file?** — Constant memory; one line at a time.
2. **What is `StopIteration`?** — Raised when a generator is exhausted.
3. **Implement a generator that yields infinite Fibonacci numbers.**

## Run

```bash
python3 example.py
```
