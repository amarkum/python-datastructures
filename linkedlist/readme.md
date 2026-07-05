# Linked List

A singly linked list implementation with common interview operations.

## Files

| File | Description |
|------|-------------|
| `linkedlistcustom.py` | Core implementation — `Node` and `LinkedList` classes |
| `caller.py` | Demo script and intersection utilities |

---

## linkedlistcustom.py

### Classes

**`Node`** — Single node with `data` and `next` pointer.

**`LinkedList`** — Singly linked list with the following methods:

| Method | Description | Time |
|--------|-------------|------|
| `add_at_head(data)` | Insert at the beginning | O(1) |
| `add_at_end(data)` | Insert at the tail | O(n) |
| `delete_at_head()` | Remove the first node | O(1) |
| `delete_by_value(value)` | Remove first node matching value | O(n) |
| `print_all()` | Print all elements | O(n) |
| `reverse()` | Reverse list in place | O(n) |
| `find_mid()` | Find middle element (slow/fast pointers) | O(n) |
| `print_mid_to_end()` | Print from middle to end | O(n) |
| `detect_loop()` | Floyd's cycle detection | O(n) |
| `is_empty()` | Check if list is empty | O(1) |

### Usage

```python
from linkedlistcustom import LinkedList

ll = LinkedList()
ll.add_at_end(1)
ll.add_at_end(2)
ll.reverse()
ll.print_all()
```

---

## caller.py

Demonstrates `LinkedList` operations and provides intersection helpers.

### Classes

**`Caller`**

| Method | Description |
|--------|-------------|
| `create_intersection(node_one, node_two)` | Creates an intersection between two lists |
| `find_intersection(head_one, head_two)` | Finds intersection node using two-pointer technique |

### Run

```bash
python3 caller.py
```

Runs delete, reverse, loop detection, and intersection demos.
