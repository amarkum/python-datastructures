# unittest.mock

## Files

| File | Description |
|------|-------------|
| `example.py` | `MagicMock`, `patch`, `side_effect`, and call assertions |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `fetch_user(user_id, db)` | Function | Dependency injected — easy to mock `db` |
| `MagicMock` | Mock class | Auto-creates attributes and records calls |
| `patch` | Context decorator | Temporarily replaces object in namespace |
| `side_effect` | Mock config | Return sequence or raise exceptions |

---

## What is mocking?

Testing in isolation by replacing dependencies (DB, API, filesystem) with fake objects that record interactions.

## Why interviewers ask

- Unit testing best practices
- Dependency injection vs patching
- How to test code with external I/O

## Key tools

| Tool | Use case |
|------|----------|
| `MagicMock()` | General-purpose mock with call tracking |
| `@patch("module.ClassName")` | Replace object during test |
| `.return_value` | Fixed return from mock |
| `.side_effect` | Callable, exception, or iterable of returns |
| `.assert_called_with()` | Verify mock was called correctly |

## Common interview questions

1. **Mock vs stub vs fake?** — Mock verifies interactions; stub returns canned data; fake has working implementation.
2. **Where to patch?** — Patch where the name is **looked up**, not where it's defined.
3. **How to mock `requests.get`?** — `@patch("mymodule.requests.get")` if imported in mymodule.

## Run

```bash
python3 example.py
```

## Related

- [context_manager](../context_manager/) — `patch` can be used as context manager
- [decorator](../decorator/) — `@patch` is a decorator
