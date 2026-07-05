# Comprehensions

## Files

| File | Description |
|------|-------------|
| `example.py` | List, dict, set, generator comprehensions and nested flatten |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `squares`, `evens` | List comps | Basic list comprehensions with optional filter |
| `word_lengths`, `inverted` | Dict comps | Build and invert dictionaries |
| `unique_lengths` | Set comp | Deduplicated values via set comprehension |
| `sum_of_squares` | Generator exp | Lazy sum without building a full list |
| `flat` | Nested comp | Flatten a 2D matrix in one expression |
| `first_long_word()` | Function | Uses walrus operator `:=` in a generator expression |

---

## What are comprehensions?

Concise syntax to build lists, dicts, sets, or generators from iterables — often replacing explicit loops.

```python
[x * 2 for x in range(5) if x % 2 == 0]
```

## Why interviewers ask

- Idiomatic Python; shows fluency
- Readability vs complexity trade-offs
- Memory: generator expressions vs list comprehensions

## Syntax reference

| Type | Syntax |
|------|--------|
| List | `[expr for x in iterable if condition]` |
| Dict | `{k: v for k, v in pairs}` |
| Set | `{expr for x in iterable}` |
| Generator | `(expr for x in iterable)` — note parentheses |

## Best practices

- Keep comprehensions **readable** — if nested or long, use a regular loop
- Use generator expressions for large data or when passing to `sum()`, `max()`, etc.
- Avoid side effects inside comprehensions

## Common interview questions

1. **List comp vs generator expression — when to use which?** — Generator for memory/large data; list when you need indexing or multiple passes.
2. **Flatten a 2D list in one line.**
3. **Is `[x for x in items]` the same as `list(items)`?** — Similar, but comp allows filtering/mapping.

## Run

```bash
python3 example.py
```

## Related

- `map()`, `filter()`, `zip()` — functional alternatives
- See [generator](../generator/) for lazy evaluation details
