# Copy & Deepcopy

## Files

| File | Description |
|------|-------------|
| `example.py` | Shallow copy, deep copy, assignment, and cyclic structures |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `copy.copy()` | Shallow copy | New outer container; inner objects shared |
| `copy.deepcopy()` | Deep copy | Recursively copies nested objects |
| Assignment `alias = a` | Alias | Same object, same id |
| `a.copy()` | List method | Shallow copy for lists |

---

## Shallow vs deep copy

| Operation | New outer object? | Nested objects shared? |
|-----------|-------------------|------------------------|
| Assignment (`b = a`) | No | Yes (same object) |
| `copy.copy(a)` | Yes | Yes |
| `copy.deepcopy(a)` | Yes | No |

## Why interviewers ask

- Bug source when passing mutable defaults or shared nested lists
- Understanding object identity vs equality
- When copies matter in data pipelines

## Common interview questions

1. **What happens when you shallow-copy a list of lists and mutate an inner list?** — Both originals and copies see the change.
2. **When do you need deepcopy?** — Nested mutables, graphs, or when full independence is required.
3. **Does `list.copy()` deep copy?** — No, it's shallow.

## Run

```bash
python3 example.py
```

## Related

- [identity_equality](../identity_equality/) — `is` vs `==`
- [mutable_default](../mutable_default/) — shared mutable state bugs
