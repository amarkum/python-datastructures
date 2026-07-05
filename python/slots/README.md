# __slots__

Restrict instance attributes to a fixed set — saves memory by eliminating per-instance `__dict__`.

## Files

| File | Description |
|------|-------------|
| `example.py` | Slotted vs regular class comparison |

---

## Descriptive Example

### Scenario

Create millions of point objects — `__slots__` reduces memory per instance.

```python
class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = PointWithSlots(1, 2)
print(hasattr(p, "__dict__"))   # False — no dict overhead

p.label = "origin"              # AttributeError — can't add new attrs
```

### Subclassing slotted classes

```python
class Point3D(PointWithSlots):
    __slots__ = ("z",)          # must declare new slots

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z
```

---

## Interview Q&A

**Q1: What does `__slots__` do?**  
A: Declares fixed instance attributes. Python stores them in a compact array instead of a `__dict__`, reducing memory and slightly speeding attribute access.

**Q2: When should you use `__slots__`?**  
A: Many homogeneous instances (ORM rows, game entities, data points) where memory is a concern. Not for general-purpose classes.

**Q3: Can slotted classes use `@property`?**  
A: Yes. Properties work normally. You can also put property names in `__slots__`.

**Q4: Trade-offs of `__slots__`?**  
A: Pros: less memory, faster access, prevents typos. Cons: no dynamic attributes, tricky multiple inheritance, weakref needs explicit slot.

**Q5: `__slots__` vs `@dataclass`?**  
A: Different purposes. Dataclass reduces boilerplate. Slots reduces memory. Combine with `@dataclass(slots=True)` in Python 3.10+.

**Q6: Does `__slots__` affect `__dict__` on the class itself?**  
A: No — the class object still has `__dict__`. Only instances lose their per-instance `__dict__`.

---

## Run

```bash
python3 example.py
```
