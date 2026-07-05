# Iterators

Objects implementing `__iter__` and `__next__` — the protocol that powers every `for` loop in Python.

## Files

| File | Description |
|------|-------------|
| `example.py` | `CountDown` and `BatchIterator` classes |

---

## Descriptive Example

### Scenario

Build a custom countdown iterator and a batch iterator that yields chunks of 3 from a list.

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in CountDown(5):
    print(n, end=" ")   # 5 4 3 2 1
```

### What `for` actually does

```python
for item in obj:
    ...

# equivalent to:
_iterator = iter(obj)       # calls obj.__iter__()
while True:
    try:
        item = next(_iterator)  # calls __next__()
    except StopIteration:
        break
```

---

## Interview Q&A

**Q1: What is the difference between iterable and iterator?**  
A: An **iterable** has `__iter__()` returning an iterator (list, str, dict). An **iterator** has both `__iter__()` (returns self) and `__next__()`.

**Q2: Is a Python list an iterator?**  
A: No. A list is iterable. Each call to `iter(my_list)` creates a fresh iterator. Once exhausted, you need a new one.

**Q3: What happens when `__next__` has no more values?**  
A: It must raise `StopIteration`. The `for` loop catches this and exits normally.

**Q4: Iterator vs generator?**  
A: Generators are a convenient way to create iterators using `yield`. Iterator classes use explicit `__iter__`/`__next__`.

**Q5: Can you iterate a custom object?**  
A: Yes — implement `__iter__` returning an object with `__next__`, or use a generator function with `yield`.

**Q6: What is an iterator exhaustion bug?**  
A: Using the same iterator twice — second loop gets nothing because the iterator is already exhausted. Call `iter()` again for a fresh one.

---

## Run

```bash
python3 example.py
```
