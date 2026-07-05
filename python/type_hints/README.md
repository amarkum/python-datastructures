# Type Hints

Annotations for static analysis — document intent for humans and tools like mypy/pyright.

## Files

| File | Description |
|------|-------------|
| `example.py` | Functions, dataclasses, generics |

---

## Descriptive Example

### Scenario

Type a user model and API functions so mypy catches passing a string where an int is expected.

```python
from dataclasses import dataclass
from typing import Optional, Generic, TypeVar

T = TypeVar("T")

@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None

def get_users(min_id: int) -> list[User]:
    return [User(id=1, name="Alice")]

def parse_id(value: int | str) -> int:
    if isinstance(value, int):
        return value
    return int(value)

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
```

Run static check: `mypy example.py`

---

## Interview Q&A

**Q1: Do type hints affect runtime?**  
A: No. They're stored in `__annotations__` and ignored at runtime unless you use a runtime validator (pydantic, beartype).

**Q2: `Optional[str]` vs `str | None`?**  
A: Equivalent. `Optional[X]` is shorthand for `Union[X, None]`. Python 3.10+ prefers `X | None`.

**Q3: What is `TypeVar` for?**  
A: Generic type variables. Preserves relationships: `def first(items: list[T]) -> T` — return type matches element type.

**Q4: What is a Protocol?**  
A: Structural subtyping — "if it has these methods, it satisfies the protocol." No inheritance required. Static check only.

**Q5: Type hints vs duck typing?**  
A: Duck typing is runtime behavior. Type hints are optional static checks. Python remains dynamically typed — hints don't enforce at runtime.

**Q6: What is `TypedDict`?**  
A: Dict with fixed key names and value types. Useful for JSON/API response shapes without full dataclass overhead.

---

## Run

```bash
python3 example.py
```
