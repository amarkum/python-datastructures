# Generators

Functions that `yield` values lazily — one at a time, without building the full result in memory.

## Files

| File | Description |
|------|-------------|
| `example.py` | Generator functions, expressions, and `.send()` |

---

## Descriptive Example

### Scenario

Generate Fibonacci numbers below 100 without storing the entire sequence in a list.

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for n in fibonacci(100):
    print(n, end=" ")
# 0 1 1 2 3 5 8 13 21 34 55 89
```

Each `yield` pauses the function and returns a value. The next call resumes right after the `yield`.

### Reading a huge file

```python
def read_lines(path):
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")   # one line in memory at a time
```

### Generator expression vs list comprehension

```python
sum(x * x for x in range(1_000_000))   # lazy — no million-item list
sum([x * x for x in range(1_000_000)]) # eager — builds full list first
```

---

## Interview Q&A

**Q1: What is the difference between a generator and a regular function?**  
A: A generator uses `yield` instead of `return`. It pauses and resumes, maintaining local state between calls. Returns a generator iterator object.

**Q2: What is `StopIteration`?**  
A: Raised when a generator is exhausted (no more values). `for` loops catch it automatically.

**Q3: Why use a generator to read a 10 GB file?**  
A: Constant memory usage — only one line/chunk in memory at a time instead of loading the entire file.

**Q4: What does `.send(value)` do?**  
A: Sends a value into the generator at the current `yield` point. Enables two-way communication between caller and generator.

**Q5: What is `yield from`?**  
A: Delegates to another generator or iterable, flattening nested generators. Used in async and recursive yield patterns.

**Q6: Generator vs iterator class?**  
A: Generators are simpler — Python auto-implements the iterator protocol. Iterator classes give more control over state and methods.

---

## Run

```bash
python3 example.py
```
