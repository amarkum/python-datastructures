# Scope (LEGB)

Python resolves names using the LEGB rule: Local → Enclosing → Global → Built-in.

## Files

| File | Description |
|------|-------------|
| `example.py` | `global`, `nonlocal`, and nested scope demos |

---

## Descriptive Example

### Scenario

A counter factory where each instance maintains its own count using `nonlocal`.

```python
def make_counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count          # modify enclosing scope, not create local
        count += step
        return count

    def get_count():
        return count

    return increment, get_count

inc, get = make_counter(100)
print(inc())    # 101
print(inc())    # 102
print(get())    # 102
```

### LEGB lookup example

```python
x = "global"

def outer():
    x = "enclosing"
    def inner():
        print(x)        # finds "enclosing" (Enclosing scope)
    inner()

outer()
```

Without `nonlocal`, `x = ...` inside `inner` would create a new **local** variable, not modify the enclosing one.

---

## Interview Q&A

**Q1: What is the LEGB rule?**  
A: Python searches names in order: **L**ocal (current function), **E**nclosing (outer functions), **G**lobal (module), **B**uilt-in (preloaded names like `len`, `print`).

**Q2: What does `global x` do?**  
A: Declares that assignments to `x` inside the function modify the module-level variable, not create a local one.

**Q3: What does `nonlocal x` do?**  
A: Declares that assignments modify the nearest enclosing (non-global) scope. Used in nested functions and closures.

**Q4: What is `UnboundLocalError`?**  
A: Occurs when you assign to a name in a function (making it local) but read it before assignment. Python treats any assignment as making the name local for the entire function.

**Q5: Does `my_list.append(x)` need `global my_list`?**  
A: No. You're mutating the object, not rebinding the name. `global` is only needed when you assign to the name itself: `my_list = []`.

**Q6: What is a closure's enclosing scope?**  
A: The scope of the outer function where the inner function was defined — not where it was called.

---

## Run

```bash
python3 example.py
```
