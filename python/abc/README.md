# Abstract Base Classes (abc)

Define interfaces that subclasses must implement — fail at instantiation if methods are missing.

## Files

| File | Description |
|------|-------------|
| `example.py` | `Shape` ABC, incomplete subclass trap, storage interface |

---

## Descriptive Example

### Scenario

Define a `Shape` interface — any concrete shape must implement `area()`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class BrokenShape(Shape):
    pass    # missing area()

rect = Rectangle(4, 5)
print(rect.area())          # 20

BrokenShape()               # TypeError: Can't instantiate abstract class
```

### Swappable implementations

```python
class Storage(ABC):
    @abstractmethod
    def save(self, data): ...
    @abstractmethod
    def load(self, key): ...

class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}
    def save(self, data):
        key = str(len(self._data))
        self._data[key] = data
        return key
    def load(self, key):
        return self._data[key]
```

---

## Interview Q&A

**Q1: What is an ABC?**  
A: Abstract Base Class — cannot be instantiated directly. Subclasses must implement all `@abstractmethod`s or instantiation raises `TypeError`.

**Q2: ABC vs duck typing?**  
A: Duck typing: "if it quacks, use it" — no formal contract. ABC: explicit interface enforced at instantiation. Both are valid Python styles.

**Q3: What is `collections.abc.Iterable`?**  
A: ABC for objects with `__iter__`. Lets you check `isinstance(obj, Iterable)` without importing concrete types.

**Q4: ABC vs Protocol (typing)?**  
A: ABC: runtime check via inheritance. Protocol: static structural typing — checked by mypy/pyright, no inheritance required.

**Q5: Can you instantiate an ABC with all methods implemented?**  
A: Yes — once all abstract methods are overridden in a concrete subclass, it can be instantiated normally.

**Q6: What is `@abstractclassmethod` / `@abstractstaticmethod`?**  
A: Variants for abstract class methods and static methods. Same rule — must be implemented in concrete subclass.

---

## Run

```bash
python3 example.py
```
