# functools

## Files

| File | Description |
|------|-------------|
| `example.py` | `lru_cache`, `partial`, `reduce`, and function pipelines |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `fibonacci(n)` | Cached function | Memoized recursion via `@lru_cache` |
| `functools.partial` | Utility | Pre-fills arguments to create specialized functions |
| `functools.reduce` | Utility | Folds iterable to single value |
| `pipeline(*functions)` | Pattern | Composes multiple functions left-to-right |

---

## What is functools?

The `functools` module provides tools for working with callable objects — caching, partial application, reduction, and decorator utilities.

## Why interviewers ask

- `@lru_cache` is a common optimization pattern
- `partial` for callbacks and configuration
- `wraps` is essential for decorators (see [decorator](../decorator/))

## Key tools

| Tool | Use case |
|------|----------|
| `@lru_cache` | Memoize pure functions with bounded cache |
| `partial(func, *args)` | Bind arguments, create new callable |
| `reduce(func, iterable)` | Aggregate iterable to one value |
| `wraps` | Preserve metadata when decorating |

## Common interview questions

1. **Implement memoization for Fibonacci.** — `@functools.lru_cache` or manual dict cache.
2. **When should you NOT use lru_cache?** — Functions with unhashable args, side effects, or mutable return values that callers mutate.
3. **Difference between `partial` and a lambda?** — `partial` preserves function metadata and introspection.

## Run

```bash
python3 example.py
```

## Related

- [decorator](../decorator/) — uses `functools.wraps`
