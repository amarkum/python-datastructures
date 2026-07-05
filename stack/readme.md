# Stack

Last In, First Out (LIFO) — like a stack of plates. Array-backed implementation with fixed capacity.

## Files

| File | Description |
|------|-------------|
| `stackcustom.py` | Core `Stack` class |
| `caller.py` | Push/pop demo with edge cases |

---

## Descriptive Example

### Scenario

Push five items onto a stack of capacity 5, try pushing a sixth (full), then pop everything off.

```python
from stackcustom import Stack

stack = Stack(3)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(99)          # prints "Stack is Full"

print(stack.pop())      # 30
print(stack.get_top())  # 20 (peek)
print(stack.pop())      # 20
print(stack.pop())      # 10
stack.pop()             # prints "Stack is Empty"
```

### Real-world uses

- Undo/redo in editors
- Function call stack (recursion)
- Balanced parentheses checking
- DFS traversal in graphs

---

## Interview Q&A

**Q1: What is the time complexity of push and pop?**  
A: O(1) for array-backed stack with a top index. Dynamic array amortized O(1) if resizing is allowed.

**Q2: Stack vs queue — key difference?**  
A: Stack is LIFO (last in, first out). Queue is FIFO (first in, first out).

**Q3: How do you implement a stack using two queues?**  
A: Enqueue new elements into q2, move all from q1 to q2, swap q1 and q2. Pop from q1 front. Push is O(n), pop is O(1).

**Q4: How do you check balanced parentheses using a stack?**  
A: Push opening brackets. On closing bracket, pop and verify match. Stack must be empty at end.

**Q5: What happens on overflow/underflow in a fixed-capacity stack?**  
A: Overflow: push when full. Underflow: pop when empty. This implementation prints a message and returns `None`.

**Q6: Can you implement a stack with O(1) getMin()?**  
A: Yes — use an auxiliary stack tracking the minimum at each level, or store tuples of (value, current_min).

---

## Run

```bash
python3 caller.py
```
