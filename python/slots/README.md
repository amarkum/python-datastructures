# __slots__

## Files

| File | Description |
|------|-------------|
| `example.py` | Slotted vs regular classes, inheritance, and memory |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `PointWithoutSlots` | Regular class | Uses `__dict__` for dynamic attributes |
| `PointWithSlots` | Slotted class | Fixed attributes `x`, `y` only |
| `ChildWithExtraSlot` | Subclass | Must declare own `__slots__` for new attrs |

---

## What is __slots__?

`__slots__` restricts instance attributes to a fixed set, eliminating per-instance `__dict__` and reducing memory usage.

```python
class Point:
    __slots__ = ("x", "y")
```

## Why interviewers ask

- Memory optimization for millions of objects (ORM rows, game entities)
- Trade-offs with pickling, multiple inheritance, and weakrefs
- Contrast with `@dataclass` and dict-based objects

## Trade-offs

| Pros | Cons |
|------|------|
| Lower memory | Cannot add attributes dynamically |
| Faster attribute access | Multiple inheritance is tricky |
| Prevents typos (`obj.lable`) | No `__dict__` unless added to slots |

## Common interview questions

1. **When would you use __slots__?** — Many homogeneous instances where memory matters.
2. **Can slotted classes use `@property`?** — Yes.
3. **Does __slots__ work with dataclass?** — Yes: `@dataclass(slots=True)` in Python 3.10+.

## Run

```bash
python3 example.py
```

## Related

- [dataclass](../dataclass/) — alternative for data containers
