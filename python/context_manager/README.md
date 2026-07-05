# Context Managers

## Files

| File | Description |
|------|-------------|
| `example.py` | Class-based and `@contextmanager` examples |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `FileManager` | Class | Opens/closes a file via `__enter__`/`__exit__` |
| `temp_value(obj, attr, new_value)` | `@contextmanager` | Temporarily sets an attribute, restores on exit |
| `Config` | Demo class | Used with `temp_value` to toggle `debug` |

---

## What is a context manager?

An object that defines `__enter__` and `__exit__`, used with the `with` statement to guarantee setup and teardown — even when exceptions occur.

```python
with open("file.txt") as f:
    data = f.read()
# file is always closed here
```

## Why interviewers ask

- Resource management (files, locks, DB connections) is daily work
- Tests understanding of exception propagation via `__exit__`
- `@contextmanager` from `contextlib` is a common pattern

## Key concepts

| Method | Role |
|--------|------|
| `__enter__` | Runs at start of `with` block; return value bound to `as` variable |
| `__exit__(exc_type, exc_val, exc_tb)` | Runs on exit; return `True` to suppress exception |
| `@contextmanager` | Write a generator with `yield`; code before = enter, `finally` = exit |

## Common interview questions

1. **Implement a context manager that suppresses a specific exception type.**
2. **Difference between `__exit__` returning True vs False?** — True suppresses the exception.
3. **When would you use `contextlib.ExitStack`?** — Managing a dynamic number of context managers.

## Run

```bash
python3 example.py
```

## Built-in examples

- `open()` — file handles
- `threading.Lock()` — acquire/release
- `unittest.mock.patch` — temporary attribute replacement
