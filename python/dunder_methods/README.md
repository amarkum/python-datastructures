# Dunder Methods (Magic Methods)

## Files

| File | Description |
|------|-------------|
| `example.py` | Operator overloading, `__repr__`/`__str__`, and custom collections |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `Vector` | Class | Implements `__add__`, `__eq__`, `__len__`, `__getitem__`, `__repr__` |
| `Stack` | Class | Extends `list` with custom `__repr__`, `push`, `pop_item` |
| `Sentence` | Class | Implements `__str__` and `__len__` |

---

## What are dunder methods?

Double-underscore methods (`__init__`, `__str__`, etc.) define how objects interact with Python's built-in operations and syntax.

## Why interviewers ask

- Custom collections and domain objects need operator overloading
- `__repr__` vs `__str__` is a classic question
- Protocol-based design (context manager, iterator, callable)

## Frequently asked methods

| Method | Triggered by |
|--------|--------------|
| `__init__` | `obj = Class()` |
| `__repr__` | `repr(obj)`, interactive shell |
| `__str__` | `str(obj)`, `print(obj)` |
| `__eq__` | `a == b` |
| `__hash__` | `hash(obj)`, use in sets/dicts |
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[key]` |
| `__call__` | `obj()` |
| `__enter__` / `__exit__` | `with obj:` |

## `__repr__` vs `__str__`

- **`__repr__`**: Unambiguous, developer-facing. Goal: `eval(repr(obj)) == obj` when possible.
- **`__str__`**: Human-readable. Falls back to `__repr__` if not defined.

## Common interview questions

1. **If you define `__eq__`, should you define `__hash__`?** — If objects are equal, they must hash equal. Mutable objects with custom `__eq__` often set `__hash__ = None`.
2. **Implement a class that supports `+` and `==`.**
3. **What makes an object callable?** — Defining `__call__`.

## Run

```bash
python3 example.py
```
