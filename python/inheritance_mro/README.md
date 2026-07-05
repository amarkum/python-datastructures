# Inheritance & MRO

## Files

| File | Description |
|------|-------------|
| `example.py` | Multiple inheritance, `super()`, and MRO inspection |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `D(B, C)` | Diamond inheritance | Classic MRO demo — order is D → B → C → A → object |
| `D.greet()` | Method | `super()` follows MRO, not just parent class |
| `Duck` | Multiple inheritance | `Animal`, `Flyer`, `Swimmer` — first `move` in MRO wins |

---

## What is MRO?

**Method Resolution Order** is the order Python searches base classes for attributes. C3 linearization ensures consistent, predictable lookup.

```python
D.__mro__  # (D, B, C, A, object)
```

## Why interviewers ask

- Diamond problem and how Python solves it
- Correct use of `super()` in cooperative inheritance
- Mixins and interface patterns

## Key concepts

| Concept | Detail |
|---------|--------|
| `super()` | Calls next class in MRO, not necessarily direct parent |
| `__mro__` | Tuple of classes in lookup order |
| Mixin | Class providing behavior, not meant to stand alone |
| `isinstance` / `issubclass` | Check type relationships |

## Common interview questions

1. **What is the MRO of `class D(B, C)` where both inherit `A`?** — D, B, C, A, object.
2. **Does `super()` call the parent class?** — No, it calls the next class in MRO.
3. **What is the diamond problem?** — Ambiguity when two parents share a grandparent; MRO resolves it.

## Run

```bash
python3 example.py
```

## Related

- [dunder_methods](../dunder_methods/) — operator overloading on inherited classes
