# Identity vs Equality

`==` compares values; `is` compares object identity (same memory address).

## Files

| File | Description |
|------|-------------|
| `example.py` | `is` vs `==`, hashability, custom equality |

---

## Descriptive Example

### Scenario

Two lists with identical contents are equal but not the same object. `None` checks must always use `is`.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True  — same values
print(a is b)   # False — different objects in memory
print(a is c)   # True  — c is an alias for a

# Always use `is` for None
value = None
if value is None:
    print("safe None check")
```

### Hashable vs unhashable

```python
hash((1, 2, 3))     # OK — tuple of ints is hashable
hash([1, 2, 3])     # TypeError — lists are mutable, unhashable

# Can't use list as dict key
{[1, 2]: "value"}   # TypeError
```

---

## Interview Q&A

**Q1: When should you use `is` vs `==`?**  
A: Use `==` for value comparison. Use `is` only for identity checks with singletons: `None`, `True`, `False`. Never use `is` for strings or numbers (except `None`).

**Q2: Why can't lists be dict keys?**  
A: Dict keys must be hashable (immutable + consistent hash). Lists are mutable — their hash would change if contents change.

**Q3: If two objects are equal, must they have the same hash?**  
A: Yes — hash contract: `a == b` implies `hash(a) == hash(b)`. Violating this breaks dicts and sets.

**Q4: What happens to `__hash__` when you define `__eq__`?**  
A: Python sets `__hash__ = None` (unhashable) unless you explicitly define `__hash__`. Mutable objects with custom equality should stay unhashable.

**Q5: Are small integers cached in CPython?**  
A: Integers `-5` to `256` are interned — `a is b` may be True for equal small ints. Never rely on this; always use `==` for value comparison.

**Q6: What is `id(obj)`?**  
A: Returns the object's identity (memory address in CPython). `a is b` is equivalent to `id(a) == id(b)`.

---

## Run

```bash
python3 example.py
```
