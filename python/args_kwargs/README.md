# *args & **kwargs

Variable-length arguments and unpacking — essential for wrappers, decorators, and flexible APIs.

## Files

| File | Description |
|------|-------------|
| `example.py` | Collection, forwarding, and unpacking demos |

---

## Descriptive Example

### Scenario

Build a user profile from required and optional fields, then forward all arguments through a logging wrapper.

```python
def build_profile(name, **kwargs):
    profile = {"name": name}
    profile.update(kwargs)
    return profile

result = build_profile("Alice", role="engineer", city="NYC", level="senior")
# {'name': 'Alice', 'role': 'engineer', 'city': 'NYC', 'level': 'senior'}
```

### Forwarding in a decorator/wrapper

```python
def log_call(func, *args, **kwargs):
    print(f"Calling {func.__name__} with {args=} {kwargs=}")
    return func(*args, **kwargs)
```

### Unpacking at call site

```python
def greet(greeting, name, punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

args = ("Hello", "Bob")
kwargs = {"punctuation": "?"}
print(greet(*args, **kwargs))   # Hello, Bob?
```

---

## Interview Q&A

**Q1: What do `*args` and `**kwargs` mean?**  
A: `*args` collects extra positional arguments into a tuple. `**kwargs` collects extra keyword arguments into a dict.

**Q2: What is the correct parameter order in a function signature?**  
A: `def f(pos_only, /, pos_or_kw, *args, kw_only, **kwargs)`. Positional-only, then regular, then `*args`, then keyword-only, then `**kwargs`.

**Q3: What does `*` alone in a signature mean?**  
A: Everything after bare `*` is keyword-only. Example: `def f(a, *, b)` — `b` cannot be passed positionally.

**Q4: How do you merge two dictionaries?**  
A: Python 3.9+: `{**d1, **d2}`. Earlier: `{**d1, **d2}` or `d1 | d2` (3.9+). Later keys override earlier ones.

**Q5: Why do decorators use `*args, **kwargs`?**  
A: So the wrapper accepts any signature and forwards all arguments to the original function unchanged.

**Q6: What is argument unpacking vs collection?**  
A: Collection: `def f(*args)` gathers args into tuple. Unpacking: `f(*my_list)` spreads sequence into positional args.

---

## Run

```bash
python3 example.py
```
