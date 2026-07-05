# Mutable Default Arguments

## Files

| File | Description |
|------|-------------|
| `example.py` | Default arg trap, None sentinel fix, and related lambda trap |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `append_bad` | Bug | Default `[]` created once, shared across calls |
| `append_good` | Fix | Uses `None` sentinel, creates fresh list per call |
| `create_multipliers_wrong/good` | Lambda trap | Late binding in loop (see [closure](../closure/)) |

---

## The trap

Default argument values are evaluated **once** at function definition time, not on each call.

```python
def f(items=[]):  # same list object every call!
    items.append(1)
    return items
```

## The fix

```python
def f(items=None):
    if items is None:
        items = []
    ...
```

## Why interviewers ask

- One of the most famous Python gotchas
- Same pattern applies to class attributes and dataclass fields
- Tests understanding of object model vs syntax

## Common interview questions

1. **What does `def f(a=[])` return on two calls?** — Second call sees mutated default.
2. **How to fix mutable defaults?** — `None` sentinel or `default_factory`.
3. **Does this apply to immutable defaults like `def f(a=0)`?** — No, ints are immutable; rebinding `a` doesn't affect other calls.

## Run

```bash
python3 example.py
```

## Related

- [dataclass](../dataclass/) — `field(default_factory=list)`
- [closure](../closure/) — late binding trap
