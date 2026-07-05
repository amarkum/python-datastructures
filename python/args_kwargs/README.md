# *args & **kwargs

## Files

| File | Description |
|------|-------------|
| `example.py` | Variable arguments, unpacking, and forwarding |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `sum_all(*args)` | Function | Collects positional args as a tuple |
| `build_profile(name, **kwargs)` | Function | Collects keyword args as a dict |
| `wrapper(func, *args, **kwargs)` | Function | Forwards all arguments to another callable |
| `greet(*args, **kwargs)` demo | Unpacking | `*` splats a sequence; `**` splats a mapping |

---

## What are *args and **kwargs?

- `*args` — collects extra **positional** arguments into a tuple
- `**kwargs` — collects extra **keyword** arguments into a dict

Unpacking reverses the process: `func(*seq, **mapping)`.

## Why interviewers ask

- Decorators and wrappers must forward arguments
- Flexible APIs and function composition
- Order rule: positional params → `*args` → keyword-only → `**kwargs`

## Signature order

```python
def f(a, b, *args, c, d=0, **kwargs):
    ...
#            ^ keyword-only after *
```

## Common interview questions

1. **Write a decorator that works with any function signature.** — Use `@wraps` and pass `*args, **kwargs`.
2. **Difference between `*args` and `**kwargs`?** — Tuple of extras vs dict of keyword extras.
3. **What does `def f(*, x)` mean?** — `x` is keyword-only; no positional args allowed after bare `*`.

## Run

```bash
python3 example.py
```

## Related

- [decorator](../decorator/) — decorators rely heavily on arg forwarding
- [closure](../closure/) — closures often wrap functions with `*args, **kwargs`
