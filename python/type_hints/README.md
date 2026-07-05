# Type Hints

## Files

| File | Description |
|------|-------------|
| `example.py` | Annotations, dataclasses, generics, and `Union` |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `greet(name, times)` | Function | Basic parameter and return type hints |
| `process_items(items)` | Function | Typed `list[int]` input and `dict` return |
| `User` | `@dataclass` | Typed fields with `Optional[str]` |
| `Box[T]` | Generic class | `TypeVar` + `Generic` with `map` method |
| `parse_id(value)` | Function | `Union[int, str]` with runtime `isinstance` check |

---

## What are type hints?

Annotations on function parameters, return values, and variables. They document intent and enable static analysis with tools like **mypy** and **pyright**. Python does **not** enforce types at runtime by default.

```python
def add(a: int, b: int) -> int:
    return a + b
```

## Why interviewers ask

- Modern codebases use typing extensively
- Shows familiarity with `Optional`, `Union`, generics, and protocols
- Distinction between runtime checks and static analysis

## Key types (typing module)

| Type | Use case |
|------|----------|
| `Optional[T]` | `T | None` — value may be missing |
| `Union[A, B]` | Value can be A or B (Python 3.10+: `A \| B`) |
| `list[int]` | Homogeneous list (3.9+ built-in generics) |
| `Callable[[int, str], bool]` | Function signature |
| `TypeVar` / `Generic` | Generic classes and functions |
| `TypedDict` | Dict with fixed key types |
| `Protocol` | Structural subtyping (duck typing for types) |

## Common interview questions

1. **Do type hints affect runtime performance?** — No. They're stored in `__annotations__` and ignored unless a type checker or runtime validator uses them.
2. **`Optional[str]` vs `str | None`?** — Equivalent in modern Python.
3. **What is `TypeVar` for?** — Preserve type relationships in generic functions/classes.

## Run

```bash
python3 example.py
```

## Static checking

```bash
pip install mypy
mypy example.py
```
