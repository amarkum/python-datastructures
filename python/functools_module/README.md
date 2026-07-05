# functools

Higher-order function utilities — caching, partial application, reduction, and decorator helpers.

## Files

| File | Description |
|------|-------------|
| `example.py` | `lru_cache`, `partial`, `reduce`, pipelines |

---

## Descriptive Example

### Scenario

Memoize Fibonacci to turn exponential recursion into linear time.

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))           # instant
print(fibonacci.cache_info())   # hits, misses, size
```

Without cache: O(2^n). With cache: O(n) — each subproblem computed once.

### Partial application

```python
def multiply(a, b, c):
    return a * b * c

double_first = functools.partial(multiply, 2)
print(double_first(5, 3))   # 2 * 5 * 3 = 30
```

---

## Interview Q&A

**Q1: What does `@lru_cache` do?**  
A: Least Recently Used cache — stores function results keyed by arguments. Repeated calls with same args return cached result instantly.

**Q2: When should you NOT use `lru_cache`?**  
A: When arguments are unhashable (lists, dicts), function has side effects, or return values are mutated by callers.

**Q3: What is `functools.partial`?**  
A: Pre-fills some arguments of a function, returning a new callable with remaining args. Useful for callbacks and configuration.

**Q4: What is `functools.wraps`?**  
A: Copies `__name__`, `__doc__`, etc. from wrapped function to wrapper. Essential for decorators (see [decorator](../decorator/)).

**Q5: What is `functools.reduce`?**  
A: Applies a binary function cumulatively: `reduce(add, [1,2,3])` → 6. Moved from builtins to functools in Python 3.

**Q6: `lru_cache` vs manual dict cache?**  
A: `lru_cache` handles eviction (maxsize), thread safety (with lock), and cache statistics. Manual dict is fine for simple cases.

---

## Run

```bash
python3 example.py
```
