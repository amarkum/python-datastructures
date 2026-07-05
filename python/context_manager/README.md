# Context Managers

Guarantee setup and cleanup using the `with` statement — even when exceptions occur.

## Files

| File | Description |
|------|-------------|
| `example.py` | Class-based and `@contextmanager` examples |

---

## Descriptive Example

### Scenario

Temporarily enable debug mode on a config object, then automatically restore the original value.

```python
from contextlib import contextmanager

class Config:
    debug = False

@contextmanager
def temp_value(obj, attr, new_value):
    old = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield obj
    finally:
        setattr(obj, attr, old)     # always runs, even on exception

cfg = Config()
print(cfg.debug)                    # False

with temp_value(cfg, "debug", True):
    print(cfg.debug)                # True — inside block

print(cfg.debug)                    # False — restored
```

### Class-based version

```python
class FileManager:
    def __enter__(self):
        self.file = open(self.path, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False    # False = don't suppress exceptions
```

---

## Interview Q&A

**Q1: What methods define a context manager?**  
A: `__enter__` (setup, return value for `as` variable) and `__exit__(exc_type, exc_val, exc_tb)` (cleanup).

**Q2: What happens if an exception occurs inside `with`?**  
A: `__exit__` is still called. If `__exit__` returns `True`, the exception is suppressed. If `False` or `None`, it propagates.

**Q3: What does `@contextmanager` do?**  
A: Turns a generator with one `yield` into a context manager. Code before `yield` = enter; `finally` after = exit.

**Q4: Why prefer `with open(...)` over manual close?**  
A: File is always closed, even if an exception occurs between open and close. Prevents resource leaks.

**Q5: What is `contextlib.ExitStack`?**  
A: Manages a dynamic number of context managers — useful when you don't know how many resources to open at compile time.

**Q6: Real-world examples of context managers?**  
A: File I/O (`open`), locks (`threading.Lock`), DB transactions, `unittest.mock.patch`, temporary directory (`tempfile`).

---

## Run

```bash
python3 example.py
```
