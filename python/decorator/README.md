# Decorators

Wrap functions or classes to add behavior (logging, timing, auth, caching) without modifying the original code.

## Files

| File | Description |
|------|-------------|
| `example.py` | Timer, parameterized, and class-based decorators |

---

## Descriptive Example

### Scenario

You need to time how long `slow_add` takes and count how many times `square` is called — without changing their logic.

```python
import functools
import time

def timer(func):
    @functools.wraps(func)          # preserves func.__name__, __doc__
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

print(slow_add(2, 3))   # slow_add took 0.1001s → 5
```

`@timer` is sugar for `slow_add = timer(slow_add)`. The wrapper is a **closure** that captures `func`.

### Parameterized decorator

```python
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")   # prints 3 times
```

---

## Interview Q&A

**Q1: What is a decorator in Python?**  
A: A callable that takes a function and returns a modified function. `@decorator` above `def f` means `f = decorator(f)`.

**Q2: Why use `@functools.wraps`?**  
A: Without it, the wrapper replaces `__name__`, `__doc__`, and other metadata. `wraps` copies them from the original function for debugging and introspection.

**Q3: Write a retry decorator that tries 3 times on failure.**  
A:
```python
def retry(times=3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == times - 1:
                        raise
        return wrapper
    return decorator
```

**Q4: Can you stack decorators? What order do they apply?**  
A: Yes. `@a @b def f` applies bottom-up: `f = a(b(f))`. `b` wraps first, then `a` wraps the result.

**Q5: Can you decorate a class?**  
A: Yes. `@dataclass`, `@total_ordering`, or custom class decorators that modify or register classes.

**Q6: Decorator vs inheritance for extending behavior?**  
A: Decorators compose behavior at runtime without subclassing. Better for cross-cutting concerns (logging, auth) applied to unrelated functions.

---

## Run

```bash
python3 example.py
```
