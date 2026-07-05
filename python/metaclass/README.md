# Metaclasses

Metaclasses are classes that create classes — they control what happens when Python sees `class Foo:`.

## Files

| File | Description |
|------|-------------|
| `example.py` | Singleton metaclass, validation, `type()` demo |

---

## Descriptive Example

### Scenario

Ensure a Database class has only one instance across the entire application.

```python
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = Database("postgres://localhost")
db2 = Database("mysql://other")
print(db1 is db2)   # True — same instance
print(db1.url)      # postgres://localhost (first call wins)
```

### Creating a class at runtime

```python
Dynamic = type("Dynamic", (), {"x": 42, "greet": lambda self: "hi"})
print(Dynamic().x)   # 42
```

---

## Interview Q&A

**Q1: What is a metaclass?**  
A: The class of a class. `MyClass.__class__` is usually `type`. Metaclasses customize class creation via `__new__` and `__init__`.

**Q2: What happens when Python executes `class Foo:`?**  
A: Body collected into namespace → metaclass `__new__` creates class object → metaclass `__init__` initializes it → name `Foo` bound to class.

**Q3: When use metaclass vs class decorator?**  
A: Metaclass: control creation of entire inheritance hierarchies. Class decorator: transform a single class. Decorator is simpler for most cases.

**Q4: What is the metaclass of `type`?**  
A: `type` itself — it's its own metaclass.

**Q5: Implement Singleton without metaclass?**  
A: Override `__new__` on the class itself, or use a module-level instance, or `@functools.lru_cache` on factory function.

**Q6: Real-world metaclass usage?**  
A: Django ORM models, dataclass generation, API registration, enforcing interfaces on subclasses. Prefer `__init_subclass__` or decorators when possible.

---

## Run

```bash
python3 example.py
```
