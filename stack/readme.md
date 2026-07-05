# Stack

An array-based stack implementation following the **Last In, First Out (LIFO)** principle.

## Files

| File | Description |
|------|-------------|
| `stackcustom.py` | Core `Stack` class |
| `caller.py` | Demo script |

---

## stackcustom.py

### Class: `Stack`

Fixed-capacity stack backed by a Python list.

| Method | Description | Time |
|--------|-------------|------|
| `push(value)` | Add element to top | O(1) |
| `pop()` | Remove and return top element | O(1) |
| `get_top()` | Peek at top without removing | O(1) |
| `is_empty()` | Check if stack is empty | O(1) |
| `is_full()` | Check if stack is at capacity | O(1) |

### Usage

```python
from stackcustom import Stack

stack = Stack(5)
stack.push(10)
print(stack.pop())  # 10
```

---

## caller.py

### Class: `StackCaller`

| Method | Description |
|--------|-------------|
| `main()` | Pushes until full, pops all, tests edge cases |

### Run

```bash
python3 caller.py
```

Demonstrates push/pop, full-stack and empty-stack handling.
