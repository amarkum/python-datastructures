# Decorators

## Files

| File | Description |
|------|-------------|
| `example.py` | Runnable examples — timer, parameterized, and class-based decorators |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `timer` | Function decorator | Times execution using `functools.wraps` |
| `repeat(times)` | Parameterized decorator | Calls the wrapped function N times |
| `CountCalls` | Class decorator | Tracks how many times a function is called |
| `slow_add`, `greet`, `square` | Demo functions | Show each decorator pattern in action |

---

## What is a decorator?

A decorator is a callable that takes a function (or class) and returns a modified version of it. Python's `@decorator` syntax is syntactic sugar for:

```python
func = decorator(func)
```

## Why interviewers ask

- Shows you understand functions as first-class objects
- Tests knowledge of closures, `*args`/`**kwargs`, and `functools.wraps`
- Real-world uses: logging, timing, auth, caching, retries

## Key concepts

| Concept | Detail |
|---------|--------|
| `@functools.wraps` | Preserves `__name__`, `__doc__`, and metadata of the wrapped function |
| Parameterized decorator | Outer function takes decorator args; inner function takes the target |
| Class decorator | Implement `__call__` or use `__init__` to receive the function |
| Stacking | `@a @b def f` applies `b` first, then `a`: `f = a(b(f))` |

## Common interview questions

1. **Write a decorator that retries a function 3 times on failure.**
2. **What happens if you forget `@functools.wraps`?** — The wrapper's name/docstring replace the original's.
3. **Can you decorate a class?** — Yes. `@dataclass`, `@property`-like patterns, or registering classes in a registry.

## Run

```bash
python3 example.py
```

## Further reading

- [PEP 318 — Decorators for Functions and Methods](https://peps.python.org/pep-0318/)
