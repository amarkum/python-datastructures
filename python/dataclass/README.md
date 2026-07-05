# Dataclass

## Files

| File | Description |
|------|-------------|
| `example.py` | `@dataclass`, frozen, ordering, and `field(default_factory)` |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `Point` | Dataclass | Basic typed data object with a method |
| `ImmutableUser` | Frozen dataclass | Immutable, supports comparison ordering |
| `Team` | Dataclass | Uses `default_factory` for mutable list field |

---

## What is a dataclass?

`@dataclass` auto-generates `__init__`, `__repr__`, and optionally `__eq__`, reducing boilerplate for data-holding classes.

## Why interviewers ask

- Modern Python idiom (3.7+)
- Relationship to `NamedTuple`, regular classes, and dicts
- `default_factory` vs mutable default argument trap

## Key concepts

| Parameter | Effect |
|-----------|--------|
| `frozen=True` | Instances are immutable (hashable if all fields hashable) |
| `order=True` | Generates comparison methods |
| `field(default_factory=list)` | Safe mutable defaults |
| `asdict()` / `replace()` | Convert to dict / copy with changes |

## Common interview questions

1. **Dataclass vs NamedTuple?** — Dataclass is mutable (unless frozen); NamedTuple is tuple subclass, immutable.
2. **Why `default_factory` instead of `members=[]`?** — Shared mutable default across instances.
3. **Does dataclass replace `__slots__`?** — No; slots still save memory for many instances.

## Run

```bash
python3 example.py
```

## Related

- [mutable_default](../mutable_default/) — the trap dataclasses solve with `default_factory`
