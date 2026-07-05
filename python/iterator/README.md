# Iterators

## Files

| File | Description |
|------|-------------|
| `example.py` | Custom iterator classes and batch iteration |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `CountDown` | Iterator class | Counts down from a start value using `__iter__`/`__next__` |
| `BatchIterator` | Iterator class | Yields fixed-size chunks from any iterable |

---

## Iterable vs iterator

| Term | Definition |
|------|------------|
| **Iterable** | Object with `__iter__()` returning an iterator (e.g. list, dict, str) |
| **Iterator** | Object with `__iter__()` (returns self) and `__next__()` |

Every `for` loop calls `iter(obj)` then repeatedly `next()` until `StopIteration`.

## Why interviewers ask

- Foundation for generators, comprehensions, and custom collections
- Explains why you can't iterate a list twice after exhausting an iterator
- Custom iterators power pagination, streaming APIs, and batch processing

## The protocol

```python
class MyIterator:
    def __iter__(self):
        return self

    def __next__(self):
        # return next value or raise StopIteration
        ...
```

## Common interview questions

1. **Is a list an iterator?** — No. A list is iterable; `iter(my_list)` returns a fresh iterator each time.
2. **Implement `__iter__` on a custom collection class.**
3. **Difference between iterator and generator?** — Generators are a convenient way to create iterators using `yield`.

## Run

```bash
python3 example.py
```
