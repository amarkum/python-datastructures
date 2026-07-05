# Lambda, map, filter & zip

## Files

| File | Description |
|------|-------------|
| `example.py` | Functional builtins and idiomatic alternatives |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `lambda` | Anonymous function | Single-expression functions |
| `map(func, iterable)` | Builtin | Apply func to every item |
| `filter(func, iterable)` | Builtin | Keep items where func returns truthy |
| `reduce(func, iterable)` | functools | Fold to single value |
| `zip(a, b)` | Builtin | Pair elements from iterables |
| `enumerate` | Builtin | Index + value pairs |

---

## Functional builtins

Often replaced by list comprehensions in modern Python, but still common in interviews and legacy code.

```python
# Equivalent styles
list(map(lambda x: x * 2, items))
[x * 2 for x in items]
```

## Why interviewers ask

- Idiomatic Python evolution (comprehensions vs map/filter)
- When lambda is appropriate (short callbacks, `key=` argument)
- Lazy vs eager: `map` returns iterator in Python 3

## Common interview questions

1. **List comp vs map — which is preferred?** — Comprehensions for readability; map when func already exists.
2. **Limitations of lambda?** — Single expression only, no statements.
3. **What does zip do with unequal lengths?** — Stops at shortest iterable.

## Run

```bash
python3 example.py
```

## Related

- [comprehension](../comprehension/) — preferred modern alternative
- [functools_module](../functools_module/) — `reduce` lives in functools
