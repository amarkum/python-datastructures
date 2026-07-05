# unittest.mock

Replace real dependencies with fakes during tests — verify interactions without hitting DB/API.

## Files

| File | Description |
|------|-------------|
| `example.py` | `MagicMock`, `patch`, `side_effect`, assertions |

---

## Descriptive Example

### Scenario

Test `fetch_user` without a real database by injecting a mock.

```python
from unittest.mock import MagicMock

def fetch_user(user_id, db):
    return db.get(user_id)

mock_db = MagicMock()
mock_db.get.return_value = {"id": 1, "name": "Alice"}

user = fetch_user(1, mock_db)
print(user)                              # {'id': 1, 'name': 'Alice'}
mock_db.get.assert_called_once_with(1)   # verify interaction
```

### Patching where name is used

```python
from unittest.mock import patch

with patch("builtins.print") as mock_print:
    print("hello")
    mock_print.assert_called_once_with("hello")
```

Patch the namespace where the name is **looked up**, not where it's defined.

---

## Interview Q&A

**Q1: Mock vs stub vs fake?**  
A: **Mock**: verifies interactions (was it called? with what args?). **Stub**: returns canned data, no verification. **Fake**: working lightweight implementation (in-memory DB).

**Q2: What is `MagicMock`?**  
A: Auto-creates attributes and methods on access. Records all calls. Returns another MagicMock for chained access.

**Q3: Where should you patch?**  
A: Where the name is looked up (import site), not where defined. If `mymodule` does `from requests import get`, patch `mymodule.get`.

**Q4: What is `side_effect`?**  
A: Instead of fixed `return_value`, can be: an exception to raise, an iterable of return values, or a callable for dynamic behavior.

**Q5: `@patch` as decorator vs context manager?**  
A: Both work. Decorator injects mock as extra argument. Context manager scopes the patch to a block.

**Q6: How to mock async functions?**  
A: `AsyncMock` from `unittest.mock` (Python 3.8+). `mock_coro = AsyncMock(return_value=result)`.

---

## Run

```bash
python3 example.py
```
