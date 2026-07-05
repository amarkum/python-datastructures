# Inheritance & MRO

Method Resolution Order determines which parent class method Python calls in multiple inheritance.

## Files

| File | Description |
|------|-------------|
| `example.py` | Diamond inheritance, `super()`, `Duck` mixin |

---

## Descriptive Example

### Scenario

Classic diamond: `D` inherits from `B` and `C`, both inherit from `A`. What order does Python search?

```python
class A:
    def greet(self):
        return "A"

class B(A):
    def greet(self):
        return f"B -> {super().greet()}"

class C(A):
    def greet(self):
        return f"C -> {super().greet()}"

class D(B, C):
    def greet(self):
        return f"D -> {super().greet()}"

print(D.__mro__)
# (<class 'D'>, <class 'B'>, <class 'C'>, <class 'A'>, <class 'object'>)

print(D().greet())   # D -> B -> C -> A
```

`super()` follows MRO — it does **not** simply call the direct parent class.

---

## Interview Q&A

**Q1: What is MRO?**  
A: Method Resolution Order — the linear order Python searches base classes for attributes/methods. Computed via C3 linearization algorithm.

**Q2: What is the diamond problem?**  
A: When two parent classes share a grandparent, which `grandparent.method()` gets called? Python's MRO resolves this deterministically.

**Q3: Does `super()` call the parent class?**  
A: No. It calls the **next** class in the MRO after the current class. In `D(B,C)`, `super()` in `B` calls `C`, not necessarily `A` directly.

**Q4: How do you inspect MRO?**  
A: `ClassName.__mro__` or `ClassName.mro()`.

**Q5: What is a mixin?**  
A: A class providing behavior but not meant to stand alone. Mixed into inheritance for reusable features (e.g., `JsonMixin`, `TimestampMixin`).

**Q6: Multiple inheritance vs composition?**  
A: Inheritance: "is-a" relationship. Composition: "has-a" — often preferred for flexibility. Favor composition when inheritance hierarchies get deep.

---

## Run

```bash
python3 example.py
```
