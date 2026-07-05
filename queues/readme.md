# Queue

A circular queue implementation following the **First In, First Out (FIFO)** principle.

## Files

| File | Description |
|------|-------------|
| `queuecustom.py` | Core `Queue` class |
| `caller.py` | Demo script |

---

## queuecustom.py

### Class: `Queue`

Fixed-capacity circular queue using a ring buffer.

| Method | Description | Time |
|--------|-------------|------|
| `enqueue(value)` | Add element to the back | O(1) |
| `dequeue()` | Remove and return front element | O(1) |
| `get_current_size()` | Return number of elements | O(1) |
| `is_empty()` | Check if queue is empty | O(1) |
| `is_full()` | Check if queue is at capacity | O(1) |

The circular index wraps using modulo arithmetic: `back = (back + 1) % max_size`.

### Usage

```python
from queuecustom import Queue

queue = Queue(5)
queue.enqueue(1)
print(queue.dequeue())  # 1
```

---

## caller.py

### Class: `QueueCaller`

| Method | Description |
|--------|-------------|
| `main()` | Enqueues until full, dequeues, re-enqueues, drains queue |

### Run

```bash
python3 caller.py
```

Demonstrates circular queue wrap-around after dequeue.
