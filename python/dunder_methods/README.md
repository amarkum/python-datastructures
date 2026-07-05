# Dunder Methods (Magic Methods)

Double-underscore methods define how objects interact with Python operators, built-ins, and syntax.

## Files

| File | Description |
|------|-------------|
| `example.py` | `Vector`, `Stack`, `Sentence` with operator overloading |

---

## Descriptive Example

### Scenario

Build a 2D vector class that supports `+`, `==`, indexing, and readable printing.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __getitem__(self, index):
        return (self.x, self.y)[index]

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)      # Vector(4, 6)
print(v1 == v2)     # False
print(v1[0])        # 1
```

### __repr__ vs __str__

```python
print(repr(v1))   # Vector(1, 2) — unambiguous, for developers
print(str(v1))    # falls back to __repr__ if __str__ not defined
```

---

## Interview Q&A

**Q1: What is the difference between `__repr__` and `__str__`?**  
A: `__repr__` is unambiguous, developer-facing (goal: valid Python to recreate object). `__str__` is human-readable, used by `print()`. `__str__` falls back to `__repr__` if not defined.

**Q2: If you define `__eq__`, should you define `__hash__`?**  
A: If objects are equal they must hash equal. Mutable objects with custom `__eq__` should set `__hash__ = None` (unhashable). Immutable objects should define both.

**Q3: How do you make an object callable?**  
A: Define `__call__`. Then `obj()` invokes it. Used for callable classes, decorators, and function-like objects.

**Q4: What triggers `__getitem__`?**  
A: `obj[key]` syntax. Also used for slicing if `__getitem__` handles slice objects.

**Q5: What is operator overloading?**  
A: Defining dunder methods like `__add__`, `__lt__`, `__len__` so built-in operators work with custom classes.

**Q6: What makes an object a context manager? Iterator?**  
A: Context manager: `__enter__` + `__exit__`. Iterator: `__iter__` + `__next__`. These are protocol-based dunder patterns.

---

## Run

```bash
python3 example.py
```
