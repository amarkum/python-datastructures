# Multiprocessing

Separate processes with independent memory — true CPU parallelism, bypassing the GIL.

## Files

| File | Description |
|------|-------------|
| `example.py` | `ProcessPoolExecutor`, `mp.Process`, queues |

---

## Descriptive Example

### Scenario

Square numbers 0–7 using four worker processes in parallel.

```python
from concurrent.futures import ProcessPoolExecutor

def square(n):
    return n * n

with ProcessPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(square, range(8)))

print(results)   # [0, 1, 4, 9, 16, 25, 36, 49]
```

Each worker runs in its own process with its own Python interpreter and GIL.

### Required guard on macOS/Windows

```python
if __name__ == "__main__":
    # spawn-based platforms re-import the module
    # without this guard, child processes spawn infinitely
    main()
```

---

## Interview Q&A

**Q1: Multiprocessing vs threading in Python?**  
A: Multiprocessing: separate processes, bypasses GIL, best for CPU-bound. Threading: shared memory, GIL-limited, best for I/O-bound.

**Q2: Why `if __name__ == "__main__"` guard?**  
A: On spawn platforms (Windows, macOS), child processes re-import the module. Without the guard, they re-execute process creation code recursively.

**Q3: How do processes share data?**  
A: `multiprocessing.Queue`, `Pipe`, `Manager` (proxy objects), or `shared_memory`. Not plain global variables.

**Q4: What is `ProcessPoolExecutor`?**  
A: Pool of worker processes. Submit tasks via `.map()` or `.submit()`. Same API pattern as `ThreadPoolExecutor`.

**Q5: What are pickling errors in multiprocessing?**  
A: Target functions and arguments must be picklable. Lambdas, local functions, and open file handles often fail. Use top-level functions.

**Q6: Process vs fork on Linux?**  
A: Linux defaults to `fork` (copy-on-write, faster). macOS/Windows use `spawn` (cleaner but slower startup). Behavior differs — always use the `__main__` guard.

---

## Run

```bash
python3 example.py
```
