# map, filter, zip & lambda

Functional-style builtins for transforming and combining iterables.

## Files

| File | Description |
|------|-------------|
| `example.py` | `map`, `filter`, `reduce`, `zip`, `enumerate` |

---

## Descriptive Example

### Scenario

Process a list of scores — double them, keep only passing scores, pair with student names.

```python
numbers = [45, 82, 67, 91, 53]
names = ["Alice", "Bob", "Carol", "Dave", "Eve"]

doubled = list(map(lambda x: x * 2, numbers))
# [90, 164, 134, 182, 106]

passing = list(filter(lambda x: x >= 60, numbers))
# [82, 67, 91]

for name, score in zip(names, numbers):
    print(f"{name}: {score}")
```

### Modern equivalent with comprehensions

```python
doubled = [x * 2 for x in numbers]
passing = [x for x in numbers if x >= 60]
```

Both are valid — comprehensions are generally preferred for readability in modern Python.

---

## Interview Q&A

**Q1: What does `map()` return in Python 3?**  
A: An iterator (lazy), not a list. Wrap with `list()` to materialize: `list(map(func, items))`.

**Q2: map/filter vs list comprehension?**  
A: Comprehensions are more Pythonic and often faster to read. `map`/`filter` are useful when the function already exists (e.g., `map(str.strip, lines)`).

**Q3: What are lambda limitations?**  
A: Single expression only — no statements, no annotations (pre-3.12), no multiline logic. Use `def` for anything complex.

**Q4: What does `zip` do with unequal-length iterables?**  
A: Stops at the shortest iterable. Use `itertools.zip_longest` to pad shorter ones.

**Q5: What is `enumerate` for?**  
A: Yields `(index, value)` pairs. `for i, item in enumerate(items, start=1)` avoids manual counter.

**Q6: What is `reduce` and where does it live?**  
A: Folds an iterable to a single value: `functools.reduce(func, items, initial)`. Example: `reduce(add, [1,2,3])` → 6.

---

## Run

```bash
python3 example.py
```
