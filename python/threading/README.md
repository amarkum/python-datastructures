# Threading & GIL

Threads share memory within a process. The GIL limits CPU parallelism but threads help with I/O-bound work.

## Files

| File | Description |
|------|-------------|
| `example.py` | Race condition, locks, `ThreadPoolExecutor` |

---

## Descriptive Example

### Scenario

Four threads increment a shared counter 100,000 times each — without a lock the result is wrong.

```python
import threading

counter = 0
lock = threading.Lock()

def unsafe_increment():
    global counter
    for _ in range(100_000):
        counter += 1          # race condition!

def safe_increment():
    global counter
    for _ in range(100_000):
        with lock:            # only one thread at a time
            counter += 1
```

Without lock: result ≈ 400,000 but often less (lost updates).  
With lock: result = 400,000 exactly.

### The GIL

Only one thread executes Python bytecode at a time per process. CPU-bound threading won't speed up computation — use [multiprocessing](../multiprocessing/) instead.

---

## Interview Q&A

**Q1: What is the GIL?**  
A: Global Interpreter Lock — a mutex in CPython allowing only one thread to execute Python bytecode at a time per process.

**Q2: Why doesn't threading speed up CPU-bound Python code?**  
A: The GIL prevents parallel bytecode execution. Threads take turns, adding overhead without CPU gain.

**Q3: When is threading still useful in Python?**  
A: I/O-bound work — network requests, file I/O, waiting on external services. Blocked I/O releases the GIL.

**Q4: How do you prevent race conditions?**  
A: `threading.Lock`, `RLock`, `Semaphore`, `Queue`, or immutable data structures. Prefer `with lock:` for auto-release.

**Q5: Thread vs process?**  
A: Threads share memory (fast communication, risk of races). Processes have separate memory (isolated, safer for CPU work, higher overhead).

**Q6: What is `ThreadPoolExecutor`?**  
A: High-level thread pool from `concurrent.futures`. Submit tasks, get `Future` objects. Cleaner than manual `Thread` management.

---

## Run

```bash
python3 example.py
```
