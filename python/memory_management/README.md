# Memory Management

## Files

| File | Description |
|------|-------------|
| `example.py` | Reference counting, cyclic GC, and weak references |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `sys.getrefcount()` | Builtin | Shows reference count (CPython) |
| `Node.__del__` | Destructor | Called when refcount hits zero (not guaranteed timing) |
| `gc.collect()` | GC | Breaks cyclic reference graphs |
| `weakref.ref()` | Weak reference | Reference that doesn't prevent collection |

---

## How Python manages memory (CPython)

1. **Reference counting** — primary mechanism; object freed when count hits 0
2. **Cycle detector (`gc` module)** — collects circular references refcount alone can't free
3. **No manual free** — unlike C/C++; developer doesn't call `free()`

## Why interviewers ask

- Explains memory leaks in long-running apps
- Weakref caches, event listeners, and observer patterns
- Contrast with Java GC or Rust ownership

## Key concepts

| Concept | Detail |
|---------|--------|
| Reference count | Increases on assignment; decreases on del / scope exit |
| Cyclic refs | Two objects reference each other — need `gc.collect()` |
| `weakref` | Observe object without keeping it alive |
| `__del__` | Unreliable for cleanup — prefer context managers |

## Common interview questions

1. **How does Python free memory?** — Reference counting + cyclic GC.
2. **Can reference cycles leak memory?** — Eventually collected by gc, but may delay until collection run.
3. **When use weakref?** — Caches, canonical mappings where you don't own the object.

## Run

```bash
python3 example.py
```

## Related

- [context_manager](../context_manager/) — preferred resource cleanup
- [slots](../slots/) — reduce memory per instance
