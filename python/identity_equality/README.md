# Identity vs Equality

## Files

| File | Description |
|------|-------------|
| `example.py` | `is` vs `==`, hashability, and custom equality |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `a`, `b`, `c` | Lists | Same value vs same object |
| Integer interning | CPython detail | Small ints `-5` to `256` may be cached |
| `HashablePerson` | Class | Defines both `__eq__` and `__hash__` for set/dict keys |
| `Person` | Class | `__eq__` only — unhashable by default |

---

## `==` vs `is`

| Operator | Compares |
|----------|----------|
| `==` | **Values** (calls `__eq__`) |
| `is` | **Identity** (same object in memory, same `id()`) |

Use `is` only for singletons: `None`, `True`, `False`.

## Hashable types

Objects usable as dict keys / set members must be **hashable** (immutable + `__hash__`).

| Hashable | Not hashable |
|----------|--------------|
| int, str, tuple (of hashables) | list, dict, set |
| frozenset | mutable custom classes without `__hash__` |

## Why interviewers ask

- Dict/set key requirements
- Defining `__eq__` disables default `__hash__` (mutable objects)
- Bug: comparing with `is` when you mean `==`

## Common interview questions

1. **Why can't lists be dict keys?** — Unhashable; mutable.
2. **If two objects are equal, must they have the same hash?** — Yes, hash contract requires it.
3. **`a is b` but `a != b`?** — Possible if `__eq__` overridden inconsistently (bad design).

## Run

```bash
python3 example.py
```

## Related

- [copy_deepcopy](../copy_deepcopy/) — copying vs aliasing
- [dunder_methods](../dunder_methods/) — `__eq__`, `__hash__`
