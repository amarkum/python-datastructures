# Mutable Default Arguments

One of Python's most famous gotchas — default values are evaluated once at function definition time.

## Files

| File | Description |
|------|-------------|
| `example.py` | The trap, the fix, and related lambda bug |

---

## Descriptive Example

### Scenario

A function that accumulates items — why does the second call remember the first?

```python
def append_bad(item, target=[]):
    target.append(item)
    return target

print(append_bad(1))   # [1]
print(append_bad(2))   # [1, 2]  ← surprise! expected [2]
```

The list `[]` is created **once** when Python defines the function. Every call shares the same list object.

### The fix

```python
def append_good(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target

print(append_good(1))   # [1]
print(append_good(2))   # [2]  ← correct
```

`None` is immutable and safe as a sentinel. A fresh list is created per call when no target is passed.

---

## Interview Q&A

**Q1: Why does `def f(a=[])` behave unexpectedly?**  
A: Default arguments are evaluated once at definition time. The same list object is reused across all calls that omit `a`.

**Q2: How do you safely use mutable defaults?**  
A: Use `None` as default, then create the mutable inside the function: `if x is None: x = []`.

**Q3: Does this affect immutable defaults like `def f(a=0)`?**  
A: No. Integers are immutable. Rebinding `a` inside the function doesn't affect other calls. The issue is mutating a shared object in place.

**Q4: Does this apply to class attributes?**  
A: Yes! `class Foo: items = []` is shared across all instances. Fix in `__init__`: `self.items = []`.

**Q5: How do dataclasses handle this?**  
A: `@dataclass` with `field(default_factory=list)` — factory called per instance, not shared.

**Q6: What is the related lambda-in-loop trap?**  
A: `[lambda x: i*x for i in range(4)]` — all lambdas bind to final `i`. Fix: `lambda x, i=i: i*x`.

---

## Run

```bash
python3 example.py
```
