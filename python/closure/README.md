# Closures

A nested function that captures variables from its enclosing scope, even after the outer function returns.

## Files

| File | Description |
|------|-------------|
| `example.py` | Multiplier factory, counter, late-binding trap |

---

## Descriptive Example

### Scenario

Create specialized multiplier functions without hardcoding the factor each time.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor       # `factor` captured from enclosing scope
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(10))   # 20
print(triple(10))   # 30
```

`multiply` is a closure — it "closes over" `factor` even though `make_multiplier` has already returned.

### Counter with `nonlocal`

```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

inc = make_counter()
print(inc(), inc(), inc())   # 1 2 3
```

### Late-binding trap

```python
# WRONG — all lambdas see i=3 (final loop value)
[f(lambda x: i * x) for i in range(4)]

# FIX — default arg captures i at definition time
[f(lambda x, i=i: i * x) for i in range(4)]
```

---

## Interview Q&A

**Q1: What is a closure?**  
A: A nested function that remembers variables from its enclosing lexical scope, even after the outer function has finished executing.

**Q2: What is the late-binding trap in loops?**  
A: Lambdas or inner functions in a loop all reference the same variable. After the loop, they all see the final value. Fix with default argument: `lambda x, i=i: ...`.

**Q3: What is `nonlocal` vs `global`?**  
A: `global` binds to module-level name. `nonlocal` binds to the nearest enclosing function scope (not global, not local).

**Q4: How do closures relate to decorators?**  
A: Decorators are closures — the wrapper function captures the original `func` from the enclosing decorator scope.

**Q5: Can closures cause memory leaks?**  
A: Yes, if a closure captures a large object and lives a long time (e.g., callbacks holding references to big data structures).

**Q6: What is a factory function?**  
A: A function that returns specialized functions/objects. Closures are the standard way to implement factories in Python.

---

## Run

```bash
python3 example.py
```
