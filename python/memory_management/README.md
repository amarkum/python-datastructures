# Memory Management

CPython uses reference counting plus a cyclic garbage collector for circular references.

## Files

| File | Description |
|------|-------------|
| `example.py` | Refcount, cyclic GC, weakref |

---

## Descriptive Example

### Scenario

Understand when objects are freed and how weak references observe without preventing collection.

```python
import sys, weakref, gc

obj = ["hello", "world"]
print(sys.getrefcount(obj) - 1)   # adjust for getrefcount's own reference

ref = obj                         # refcount +1
alias = obj                       # refcount +1

del ref, alias, obj               # refcount → 0 → object freed

# Weak reference — doesn't prevent collection
data = ["important"]
weak = weakref.ref(data)
print(weak() is not None)   # True
del data
print(weak() is None)       # True — object collected
```

### Cyclic references

```python
a = []
b = []
a.append(b)
b.append(a)
del a, b
gc.collect()    # cycle detector frees both
```

Reference counting alone can't free cycles — the cyclic GC handles them.

---

## Interview Q&A

**Q1: How does Python manage memory?**  
A: Primary: reference counting (increment on assign, decrement on del/scope exit; free at zero). Secondary: cyclic GC for circular references.

**Q2: Can Python have memory leaks?**  
A: Yes — global references, closures capturing large objects, C extensions, or cycles with `__del__` methods that prevent GC collection.

**Q3: What is `weakref`?**  
A: Reference that doesn't increment refcount. Useful for caches and observers — object can be collected when no strong refs remain.

**Q4: Is `__del__` reliable for cleanup?**  
A: No. Call order is undefined, may not run at interpreter shutdown, and can resurrect objects. Prefer context managers and `try/finally`.

**Q5: What is `gc.collect()`?**  
A: Forces a full garbage collection cycle. Useful after deleting large cyclic structures. Usually not needed in normal code.

**Q6: Python vs Java GC?**  
A: Python: refcount (deterministic, immediate) + cycle detector. Java: tracing GC (generational). Python has no manual `free()` — developer doesn't manage memory directly.

---

## Run

```bash
python3 example.py
```
