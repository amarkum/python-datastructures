# Abstract Base Classes (abc)

## Files

| File | Description |
|------|-------------|
| `example.py` | `ABC`, `@abstractmethod`, and interface enforcement |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `Shape` | ABC | Defines abstract `area()` and `perimeter()` |
| `Rectangle` | Concrete class | Implements all abstract methods |
| `InvalidShape` | Incomplete class | Cannot be instantiated — missing methods |
| `Storage` / `MemoryStorage` | Interface pattern | Swap implementations behind common ABC |

---

## What is abc?

The `abc` module lets you define **abstract base classes** — classes that cannot be instantiated until all `@abstractmethod`s are implemented.

## Why interviewers ask

- Interface design and polymorphism
- Difference from duck typing ("if it walks like a duck...")
- Used in stdlib: `collections.abc.Iterable`, `Sequence`, etc.

## Key concepts

| Concept | Detail |
|---------|--------|
| `ABC` | Base class to inherit from |
| `@abstractmethod` | Must be overridden in subclass |
| `register()` | Virtual subclass (duck typing registration) |
| `collections.abc` | Ready-made ABCs for protocols |

## ABC vs duck typing

- **Duck typing**: "Don't check type, check behavior at runtime"
- **ABC**: Explicit contract; fail at instantiation if incomplete

## Common interview questions

1. **Can you instantiate a class with unimplemented abstract methods?** — No, `TypeError` at instantiation.
2. **What is `collections.abc.Mapping`?** — ABC for dict-like objects.
3. **ABC vs Protocol (typing)?** — ABC is runtime checkable; Protocol is static structural typing.

## Run

```bash
python3 example.py
```

## Related

- [inheritance_mro](../inheritance_mro/) — MRO with abstract classes
- [type_hints](../type_hints/) — `Protocol` for structural subtyping
