# Properties & Descriptors

Control attribute access with validation, computed fields, and the descriptor protocol.

## Files

| File | Description |
|------|-------------|
| `example.py` | `@property`, custom descriptors, validation |

---

## Descriptive Example

### Scenario

A `Circle` class where radius is validated on set and area is computed automatically.

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

c = Circle(5)
print(c.area)       # 78.54
c.radius = 10
print(c.area)       # 314.16
c.radius = -1       # ValueError
```

### Custom descriptor

```python
class ValidatedAttribute:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Must be positive")
        obj.__dict__[self.name] = value
```

---

## Interview Q&A

**Q1: What is `@property`?**  
A: Decorator that turns a method into a managed attribute. Supports getter, setter, and deleter. Callers use `obj.x` syntax, not `obj.x()`.

**Q2: How does `@property` work internally?**  
A: It returns a descriptor object implementing `__get__`, `__set__`, `__delete__`. Python invokes these on attribute access.

**Q3: Property vs public attribute?**  
A: Property adds validation/computation without changing the public API. You can start with public attr and migrate to property without breaking callers.

**Q4: What is the descriptor protocol?**  
A: Object defining `__get__`, `__set__`, or `__delete__`. Class-level descriptors are invoked automatically on instance attribute access.

**Q5: What is `__set_name__`?**  
A: Called when descriptor is assigned to a class attribute (Python 3.6+). Lets descriptor know its attribute name automatically.

**Q6: Real-world descriptor examples?**  
A: `@property`, ORM field types (Django/SQLAlchemy), validated attributes, lazy-loaded attributes, bound methods.

---

## Run

```bash
python3 example.py
```
