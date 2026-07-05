# Scope (LEGB)

## Files

| File | Description |
|------|-------------|
| `example.py` | LEGB lookup, `global`, `nonlocal`, and nested scopes |

### example.py walkthrough

| Symbol | Type | Description |
|--------|------|-------------|
| `outer()` / `inner()` | Nested functions | `nonlocal` modifies enclosing scope |
| `global_demo()` | Function | `global` modifies module-level name |
| `make_counter()` | Factory | Closure + `nonlocal` for mutable state |
| `legb_demo()` | Function | Shows local vs built-in lookup |

---

## LEGB rule

Python resolves names in this order:

1. **L**ocal — inside current function
2. **E**nclosing — nested outer functions
3. **G**lobal — module level
4. **B**uilt-in — `len`, `print`, etc.

## Why interviewers ask

- Closures and decorators depend on scope
- `global` vs `nonlocal` confusion
- UnboundLocalError when assigning to a name Python treats as local

## Key concepts

| Keyword | Scope modified |
|---------|----------------|
| `global x` | Module-level name in current module |
| `nonlocal x` | Name in nearest enclosing (non-global) scope |
| No keyword | Assignment creates/overwrites **local** variable |

## Common interview questions

1. **What does `nonlocal` do?** — Binds assignment to enclosing scope (not global, not local).
2. **Why `UnboundLocalError`?** — Function assigns to a name, so Python treats it as local, but it's read before assignment.
3. **Are list mutations `global`?** — No; `items.append(x)` mutates object without rebinding `items`.

## Run

```bash
python3 example.py
```

## Related

- [closure](../closure/) — closures capture enclosing variables
- [mutable_default](../mutable_default/) — scope-related gotcha
