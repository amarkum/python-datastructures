# Exception Handling

## Files

| File | Description |
|------|-------------|
| `example.py` | try/except/else/finally, custom exceptions, and chaining |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `ValidationError` | Exception class | Custom error with `field` attribute |
| `divide(a, b)` | Function | Raises `ZeroDivisionError` with custom message |
| `parse_age(value)` | Function | Chains `ValueError` into `ValidationError` via `raise ... from` |
| `read_config(path)` | Function | Demonstrates `else` and `finally` clauses |
| `Resource` | Class | Context manager used alongside exception handling |

---

## Basics

```python
try:
    risky_operation()
except SpecificError as e:
    handle(e)
else:
    # runs only if no exception was raised
    on_success()
finally:
    # always runs (cleanup)
    cleanup()
```

## Why interviewers ask

- Robust error handling is essential in production code
- `raise ... from` for exception chaining
- Custom exception hierarchies for domain errors

## Key concepts

| Concept | Detail |
|---------|--------|
| `except Exception` | Catches broad exceptions — avoid unless re-raising |
| `raise ... from cause` | Chain exceptions; preserves traceback |
| `else` clause | Runs if try block succeeds (no except triggered) |
| `finally` | Always executes; use for cleanup |
| Custom exceptions | Subclass `Exception`; add attributes as needed |

## Exception hierarchy (simplified)

```
BaseException
├── SystemExit, KeyboardInterrupt
└── Exception
    ├── ValueError, TypeError, KeyError
    ├── IOError / OSError
    └── Your custom errors
```

## Common interview questions

1. **Difference between `except Exception` and bare `except:`?** — Bare except catches everything including `KeyboardInterrupt`; never use it.
2. **When is the `else` clause useful?** — Code that should run only on success, not inside try (which would catch its own errors).
3. **What does `raise X from Y` do?** — Sets `__cause__` for clearer error chains.

## Run

```bash
python3 example.py
```

## Best practices

- Catch specific exceptions, not bare `Exception` unless re-raising
- Use custom exception classes for domain logic
- Prefer context managers over manual try/finally for resources
