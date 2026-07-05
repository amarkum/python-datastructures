# Metaclasses

## Files

| File | Description |
|------|-------------|
| `example.py` | Singleton metaclass, validation metaclass, and `type()` demo |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `SingletonMeta` | Metaclass | Ensures only one instance per class |
| `Database` | Class | Uses `SingletonMeta` — second call returns same instance |
| `ValidatedMeta` | Metaclass | Raises `TypeError` if required attrs are missing |
| `Plugin` | Class | Validated by `ValidatedMeta` |
| `Dynamic` | Class via `type()` | Created at runtime without `class` statement |

---

## What is a metaclass?

A metaclass is the **class of a class**. Just as `instance.__class__` is `MyClass`, `MyClass.__class__` is usually `type`. Metaclasses control **how classes are created**.

```python
class MyClass(metaclass=MyMeta):
    pass
# MyMeta.__new__ / __init__ run when MyClass is defined
```

## Why interviewers ask

- Advanced OOP; shows deep Python knowledge
- Used in frameworks: Django ORM, dataclasses internals, ABC registration
- Often asked as "what happens when Python sees `class Foo`?"

## Class creation flow (simplified)

1. Python collects the class body into a namespace dict
2. Metaclass `__new__` creates the class object
3. Metaclass `__init__` initializes it
4. Class object is bound to the name `Foo`

## Key concepts

| Concept | Detail |
|---------|--------|
| `type(name, bases, dict)` | Built-in way to create a class at runtime |
| `__new__` on metaclass | Called before the class object exists |
| `__init__` on metaclass | Called after class object is created |
| Default metaclass | `type` |

## Common interview questions

1. **When would you use a metaclass vs a class decorator?** — Metaclass for inheritance hierarchies; decorator for single-class transformation.
2. **Implement a Singleton using a metaclass.**
3. **What is the metaclass of `type`?** — `type` (itself).

## Run

```bash
python3 example.py
```

## Note

Prefer simpler alternatives when possible: `@dataclass`, `__init_subclass__`, or class decorators often suffice.
