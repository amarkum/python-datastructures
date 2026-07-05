# Queue

First In, First Out (FIFO) — circular ring buffer with fixed capacity. Front and back wrap using modulo.

## Files

| File | Description |
|------|-------------|
| `queuecustom.py` | Core `Queue` class |
| `caller.py` | Enqueue/dequeue demo with wrap-around |

---

## Descriptive Example

### Scenario

Fill a queue of capacity 5, dequeue two items (freeing space at the front), then enqueue more — indices wrap around the ring buffer.

```python
from queuecustom import Queue

queue = Queue(5)
for i in range(1, 6):
    queue.enqueue(i)        # [1,2,3,4,5]

queue.dequeue()             # removes 1
queue.dequeue()             # removes 2

queue.enqueue(10)           # wraps to front slot
queue.enqueue(11)

while not queue.is_empty():
    print(queue.dequeue())  # 3, 4, 5, 10, 11
```

### Why circular?

Without wrapping, dequeue would leave empty slots at the front forever. Modulo arithmetic reuses them: `back = (back + 1) % max_size`.

---

## Interview Q&A

**Q1: What is the time complexity of enqueue and dequeue?**  
A: O(1) for circular array implementation. O(1) amortized for linked-list queue.

**Q2: Queue vs stack?**  
A: Queue is FIFO — first added is first removed. Stack is LIFO.

**Q3: How does a circular queue avoid wasting space?**  
A: Front and back indices wrap with `% capacity`, reusing slots freed by dequeue.

**Q4: How do you implement a queue using two stacks?**  
A: Push to stack1 for enqueue. For dequeue, if stack2 empty, pop all from stack1 into stack2, then pop stack2. Amortized O(1) per operation.

**Q5: What is a deque (double-ended queue)?**  
A: Allows O(1) insert/delete at both ends. Python's `collections.deque` is the standard choice.

**Q6: Where are queues used in practice?**  
A: BFS graph traversal, task schedulers, message brokers, print spoolers, rate limiting buffers.

---

## Run

```bash
python3 caller.py
```
