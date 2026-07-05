# Properties & Descriptors

## Files

| File | Description |
|------|-------------|
| `example.py` | `@property`, custom descriptors, and validation |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `Celsius` | Descriptor | Stores temperature with validation on set |
| `Temperature` | Class | Uses `Celsius` descriptor + `fahrenheit` property |
| `Circle` | Class | `@property` for `radius` and computed `area` |
| `ValidatedAttribute` | Descriptor | Reusable descriptor with custom validator |
| `Product` | Class | Uses `ValidatedAttribute` for positive `price` |

---

## What is a property?

`@property` turns a method into an attribute-like accessor with optional getter, setter, and deleter. It enables validation and computed fields without changing the public API.

```python
@property
def radius(self):
    return self._radius

@radius.setter
def radius(self, value):
    if value <= 0:
        raise ValueError("invalid")
    self._radius = value
```

## What is a descriptor?

A descriptor is an object defining `__get__`, `__set__`, or `__delete__`. Class attributes that are descriptors are invoked automatically on attribute access.

Properties are implemented using descriptors under the hood.

## Why interviewers ask

- Encapsulation without ugly `get_`/`set_` methods
- How `@property` works internally
- Framework patterns (ORM fields, validated attributes)

## Descriptor protocol

| Method | Called when |
|--------|-------------|
| `__get__(self, obj, type)` | Reading `obj.attr` |
| `__set__(self, obj, value)` | Assigning `obj.attr = value` |
| `__delete__(self, obj)` | `del obj.attr` |
| `__set_name__(self, owner, name)` | Descriptor assigned to class (Python 3.6+) |

## Common interview questions

1. **Difference between `@property` and a public attribute?** — Property adds validation/computation; can migrate from public attr without breaking callers.
2. **How does `@property` work internally?** — It returns a descriptor object.
3. **Implement a descriptor that validates positive integers.**

## Run

```bash
python3 example.py
```
