# Linked List

A singly linked list — each node stores data and a pointer to the next node. Common in interviews for reversal, cycle detection, and two-pointer problems.

## Files

| File | Description |
|------|-------------|
| `linkedlistcustom.py` | `Node` and `LinkedList` implementation |
| `caller.py` | Demo + intersection utilities |

---

## Descriptive Example

### Scenario

Build a list `2 → 4 → 6 → 7`, delete `4`, reverse it, and find the middle element.

### Step-by-step

```python
from linkedlistcustom import LinkedList

ll = LinkedList()
for value in [2, 4, 6, 7]:
    ll.add_at_end(value)

ll.delete_by_value(4)   # 2 → 6 → 7
ll.reverse()            # 7 → 6 → 2
print(ll.find_mid())    # 6 (slow/fast pointers)
```

### Floyd's cycle detection

If the last node points back to an earlier node, `detect_loop()` returns `True` using slow/fast pointers — O(n) time, O(1) space.

### Intersection of two lists

`Caller.find_intersection(head_a, head_b)` — when two lists merge, both pointers switch heads after reaching the end. They meet at the intersection or both become `None`.

```bash
python3 caller.py
```

---

## Interview Q&A

**Q1: What is the time complexity of inserting at the head vs tail of a singly linked list?**  
A: Head insert is O(1). Tail insert is O(n) because you must traverse to the last node (unless you keep a tail pointer).

**Q2: How do you reverse a linked list in place?**  
A: Iterate with three pointers — `prev`, `current`, `next`. Set `current.next = prev`, then advance all three. Update `head` to the last `prev`.

**Q3: How does Floyd's cycle detection work?**  
A: Slow moves 1 step, fast moves 2 steps per iteration. If there's a cycle, fast eventually equals slow. If fast reaches `None`, no cycle.

**Q4: How do you find the middle of a linked list in one pass?**  
A: Slow pointer moves 1 step, fast moves 2 steps. When fast reaches the end, slow is at the middle.

**Q5: Linked list vs array — when prefer which?**  
A: Linked list: frequent inserts/deletes at known positions, unknown size. Array: random access, cache locality, less memory overhead per element.

**Q6: How do you find the intersection node of two linked lists?**  
A: Two pointers start at each head. When one reaches the end, redirect to the other list's head. They meet at intersection or both become `None` after equal total steps.

---

## Run

```bash
python3 caller.py
```
