# Comprehensions

Concise syntax to transform and filter iterables into lists, dicts, sets, or generators.

## Files

| File | Description |
|------|-------------|
| `example.py` | List, dict, set, generator comps, nested flatten |

---

## Descriptive Example

### Scenario

From a list of words, build a length map, filter long words, and sum squares without building a huge list.

```python
words = ["python", "go", "javascript", "rust"]

# dict comprehension
lengths = {w: len(w) for w in words}
# {'python': 6, 'go': 2, 'javascript': 10, 'rust': 4}

# list comprehension with filter
long_words = [w for w in words if len(w) > 4]
# ['python', 'javascript']

# generator expression — lazy, memory efficient
total = sum(len(w) ** 2 for w in words)

# flatten 2D matrix
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]
```

---

## Interview Q&A

**Q1: List comprehension vs generator expression?**  
A: List comp `[x for x in items]` builds the full list in memory. Generator `(x for x in items)` yields one at a time — use for large data or as argument to `sum()`, `max()`, etc.

**Q2: When should you NOT use a comprehension?**  
A: When logic is complex, nested deeply, or has side effects. A regular loop is more readable for multi-step logic.

**Q3: How do you flatten a 2D list in one line?**  
A: `[item for row in matrix for item in row]`.

**Q4: Dict comprehension syntax?**  
A: `{key_expr: val_expr for item in iterable if condition}`.

**Q5: Is `[x for x in items]` the same as `list(items)`?**  
A: Similar for simple iteration, but comprehension allows filtering (`if`) and transformation (`x * 2`).

**Q6: Can comprehensions have side effects?**  
A: Technically yes (`[print(x) for x in items]`), but it's bad practice. Use a regular loop for side effects.

---

## Run

```bash
python3 example.py
```
