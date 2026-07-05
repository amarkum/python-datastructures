# Closures

## Files

| File | Description |
|------|-------------|
| `example.py` | Closures, `nonlocal`, and the late-binding trap |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `make_multiplier(factor)` | Factory | Returns a function that multiplies by `factor` |
| `make_counter(start)` | Factory | Returns `increment` and `get_count` sharing state via `nonlocal` |
| `make_multipliers_wrong()` | Trap demo | Lambdas in loop — all bind to final `i` |
| `make_multipliers_correct()` | Fix demo | Default arg `i=i` captures value at definition time |

---

## What is a closure?

A closure is a nested function that remembers variables from its enclosing scope, even after the outer function has returned.

```python
def outer(x):
    def inner(y):
        return x + y  # x is "closed over"
    return inner
```

## Why interviewers ask

- Decorators are built on closures
- Factory functions (e.g. `make_multiplier(3)`) are a common pattern
- The **late binding** loop trap appears frequently in interviews

## Key concepts

| Concept | Detail |
|---------|--------|
| Enclosing scope | Variables from outer function accessible in inner function |
| `nonlocal` | Modify a variable in an enclosing (non-global) scope |
| Late binding | Lambdas in a loop all see the **final** value of the loop variable unless captured via default arg |

## Late binding fix

```python
# Wrong — all lambdas use i=4
[f(lambda x: i * x) for i in range(5)]

# Correct — default arg captures i at definition time
[f(lambda x, i=i: i * x) for i in range(5)]
```

## Common interview questions

1. **Explain the output of lambdas created inside a for loop.**
2. **What is `nonlocal` vs `global`?**
3. **How do closures relate to decorators?**

## Run

```bash
python3 example.py
```
