# Exception Handling

Structured error handling with try/except/else/finally, custom exceptions, and exception chaining.

## Files

| File | Description |
|------|-------------|
| `example.py` | Custom exceptions, chaining, else/finally |

---

## Descriptive Example

### Scenario

Parse user age from input — convert errors into a domain-specific `ValidationError` with clear context.

```python
class ValidationError(Exception):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

def parse_age(value):
    try:
        age = int(value)
    except ValueError as e:
        raise ValidationError("age", f"must be integer, got {value!r}") from e

    if age < 0 or age > 150:
        raise ValidationError("age", "must be between 0 and 150")
    return age

parse_age("twenty")   # ValidationError: age: must be integer, got 'twenty'
                      # __cause__ links to original ValueError
```

### try/except/else/finally flow

```python
try:
    result = risky_operation()
except SpecificError as e:
    handle(e)
else:
    on_success(result)      # runs only if NO exception
finally:
    cleanup()               # ALWAYS runs
```

---

## Interview Q&A

**Q1: Difference between `except Exception` and bare `except:`?**  
A: Bare `except:` catches everything including `KeyboardInterrupt` and `SystemExit`. Never use it. Catch specific exceptions or `Exception` when re-raising.

**Q2: When is the `else` clause useful?**  
A: Code that should run only on success — kept out of `try` so its own exceptions aren't caught by the handler above.

**Q3: What does `raise NewError(...) from original` do?**  
A: Sets `__cause__` on the new exception, preserving the original traceback chain for debugging.

**Q4: What is the exception hierarchy?**  
A: `BaseException` → `Exception` → specific errors (`ValueError`, `TypeError`, etc.). Catch subclasses, not `BaseException`.

**Q5: When should you create custom exception classes?**  
A: For domain-specific errors (validation, auth, payment) that callers can catch specifically. Add attributes like `field` or `code`.

**Q6: finally vs context manager?**  
A: Both guarantee cleanup. Context managers (`with`) are preferred — cleaner syntax and composable via `ExitStack`.

---

## Run

```bash
python3 example.py
```
