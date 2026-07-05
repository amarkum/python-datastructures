# python-datastructures

A hands-on Python repo for **data structures** and **interview topics**. Every folder has runnable code, a README, and short examples below.

**Requirements:** Python 3.8+ · No external dependencies

---

## Quick run

```bash
# Data structures
python3 linkedlist/caller.py
python3 stack/caller.py
python3 queues/caller.py
python3 tree/caller.py

# Python interview topic
cd python/decorator && python3 example.py
```

---

## Data structures

### [Linked List](./linkedlist/)

Linear collection of nodes. Each node holds data and a pointer to the next node.

```python
from linkedlistcustom import LinkedList

ll = LinkedList()
ll.add_at_end(10)
ll.add_at_end(20)
ll.reverse()          # in-place reversal
ll.detect_loop()      # Floyd's cycle detection
ll.find_mid()         # slow/fast pointer
```

**Run:** `python3 linkedlist/caller.py` · **Docs:** [linkedlist/README.md](./linkedlist/README.md)

---

### [Stack](./stack/)

Last In, First Out (LIFO). Array-backed with fixed capacity.

```python
from stackcustom import Stack

stack = Stack(5)
stack.push(10)
stack.push(20)
print(stack.pop())    # 20
print(stack.get_top())  # peek without removing
```

**Run:** `python3 stack/caller.py` · **Docs:** [stack/README.md](./stack/README.md)

---

### [Queue](./queues/)

First In, First Out (FIFO). Circular ring buffer.

```python
from queuecustom import Queue

queue = Queue(5)
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())  # 1
```

**Run:** `python3 queues/caller.py` · **Docs:** [queues/README.md](./queues/README.md)

---

### [Binary Search Tree](./tree/)

Ordered tree — left subtree < node < right subtree. Supports insert, search, delete.

```python
from binarysearchtreecustom import BinarySearchTree

bst = BinarySearchTree()
bst.add(5)
bst.add(3)
bst.add(7)
print(bst.search(3))   # True
bst.delete(3)
bst.print_tree(bst.root)
```

**Run:** `python3 tree/caller.py` · **Docs:** [tree/README.md](./tree/README.md)

---

## Python interview topics

Full index: [python/README.md](./python/README.md)

---

### Core language

#### [Decorators](./python/decorator/)

Wrap a function to extend behavior without changing its source.

```python
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result
    return wrapper

@timer
def work():
    ...
```

**Run:** `python3 python/decorator/example.py`

---

#### [Context Managers](./python/context_manager/)

Guarantee setup/teardown with the `with` statement.

```python
from contextlib import contextmanager

@contextmanager
def temp_value(obj, attr, new_value):
    old = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield obj
    finally:
        setattr(obj, attr, old)

with temp_value(config, "debug", True):
    run_tests()
```

**Run:** `python3 python/context_manager/example.py`

---

#### [Generators](./python/generator/)

Lazy iteration with `yield` — constant memory for large data.

```python
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

for n in fibonacci(100):
    print(n)
```

**Run:** `python3 python/generator/example.py`

---

#### [Iterators](./python/iterator/)

Objects with `__iter__` and `__next__` — the protocol behind `for` loops.

```python
class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1
```

**Run:** `python3 python/iterator/example.py`

---

#### [Closures](./python/closure/)

Inner functions that remember variables from an enclosing scope.

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

double = make_multiplier(2)
print(double(10))  # 20
```

**Run:** `python3 python/closure/example.py`

---

#### [*args & **kwargs](./python/args_kwargs/)

Flexible signatures and argument forwarding.

```python
def build_profile(name, **kwargs):
    return {"name": name, **kwargs}

def wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

build_profile("Alice", role="engineer", city="NYC")
greet(*("Hello", "Bob"), **{"punctuation": "?"})
```

**Run:** `python3 python/args_kwargs/example.py`

---

#### [Scope (LEGB)](./python/scope/)

Name lookup order: **L**ocal → **E**nclosing → **G**lobal → **B**uilt-in.

```python
count = 0

def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

**Run:** `python3 python/scope/example.py`

---

#### [Comprehensions](./python/comprehension/)

Concise way to build lists, dicts, sets, and generators.

```python
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
word_map = {w: len(w) for w in ["python", "go"]}
total = sum(x ** 2 for x in range(1000))  # generator — lazy
```

**Run:** `python3 python/comprehension/example.py`

---

#### [map, filter, zip](./python/lambda_map_filter/)

Functional-style builtins (often replaced by comprehensions today).

```python
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
for name, score in zip(names, scores):
    print(name, score)
```

**Run:** `python3 python/lambda_map_filter/example.py`

---

#### [Exception Handling](./python/exception_handling/)

Structured error handling with try/except/else/finally.

```python
try:
    result = divide(a, b)
except ZeroDivisionError as e:
    print(f"Caught: {e}")
else:
    print(f"Result: {result}")
finally:
    cleanup()
```

**Run:** `python3 python/exception_handling/example.py`

---

#### [Mutable Default Arguments](./python/mutable_default/)

Default values are evaluated **once** at definition time — a classic trap.

```python
# BUG — same list shared across calls
def append_bad(item, target=[]):
    target.append(item)
    return target

# FIX — use None sentinel
def append_good(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target
```

**Run:** `python3 python/mutable_default/example.py`

---

#### [is vs ==](./python/identity_equality/)

`==` compares values; `is` compares object identity (same memory).

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True  — same values
print(a is b)  # False — different objects

x = None
if x is None:  # always use `is` for None
    ...
```

**Run:** `python3 python/identity_equality/example.py`

---

#### [Copy & Deepcopy](./python/copy_deepcopy/)

Shallow copy shares nested objects; deep copy is fully independent.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)
# shallow affected, deep unchanged
```

**Run:** `python3 python/copy_deepcopy/example.py`

---

### OOP & classes

#### [Dunder Methods](./python/dunder_methods/)

Magic methods control operators, printing, and protocol behavior.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
```

**Run:** `python3 python/dunder_methods/example.py`

---

#### [Inheritance & MRO](./python/inheritance_mro/)

Method Resolution Order — how Python searches base classes.

```python
class B(A):
    def greet(self):
        return f"B -> {super().greet()}"

class D(B, C):
    pass

print(D.__mro__)  # (D, B, C, A, object)
```

**Run:** `python3 python/inheritance_mro/example.py`

---

#### [Metaclasses](./python/metaclass/)

Classes that create classes — control class construction.

```python
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass
```

**Run:** `python3 python/metaclass/example.py`

---

#### [Properties & Descriptors](./python/property_descriptor/)

Validated attributes and computed fields without breaking the API.

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2
```

**Run:** `python3 python/property_descriptor/example.py`

---

#### [Dataclasses](./python/dataclass/)

Auto-generated `__init__`, `__repr__`, and `__eq__` for data objects.

```python
from dataclasses import dataclass, field

@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)

@dataclass(frozen=True)
class Point:
    x: float
    y: float
```

**Run:** `python3 python/dataclass/example.py`

---

#### [__slots__](./python/slots/)

Fixed attributes — saves memory by removing per-instance `__dict__`.

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

**Run:** `python3 python/slots/example.py`

---

#### [Abstract Base Classes](./python/abc/)

Enforce interfaces with `@abstractmethod`.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def area(self):
        return self.width * self.height
```

**Run:** `python3 python/abc/example.py`

---

### Concurrency & async

#### [Threading & GIL](./python/threading/)

Threads share memory. The GIL limits CPU parallelism in CPython.

```python
import threading

lock = threading.Lock()
counter = 0

def safe_increment():
    global counter
    with lock:
        counter += 1
```

**Run:** `python3 python/threading/example.py`

---

#### [Multiprocessing](./python/multiprocessing/)

Separate processes for CPU-bound work — bypasses the GIL.

```python
from concurrent.futures import ProcessPoolExecutor

with ProcessPoolExecutor(max_workers=4) as pool:
    results = list(pool.map(square, range(8)))
```

**Run:** `python3 python/multiprocessing/example.py`

---

#### [Async / Await](./python/async_await/)

Cooperative I/O concurrency on a single thread.

```python
import asyncio

async def fetch(name):
    await asyncio.sleep(0.1)
    return f"result-{name}"

async def main():
    results = await asyncio.gather(fetch("A"), fetch("B"))
    print(results)

asyncio.run(main())
```

**Run:** `python3 python/async_await/example.py`

---

### Standard library & tooling

#### [functools](./python/functools_module/)

Caching, partial application, and function utilities.

```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

double = functools.partial(multiply, 2)
```

**Run:** `python3 python/functools_module/example.py`

---

#### [Type Hints](./python/type_hints/)

Static annotations for tooling (mypy, pyright) — not enforced at runtime.

```python
from dataclasses import dataclass
from typing import Optional

def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()

@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None
```

**Run:** `python3 python/type_hints/example.py`

---

#### [unittest.mock](./python/unittest_mock/)

Replace dependencies in tests with fakes that record calls.

```python
from unittest.mock import MagicMock, patch

mock_db = MagicMock()
mock_db.get.return_value = {"id": 1, "name": "Alice"}
user = fetch_user(1, mock_db)
mock_db.get.assert_called_once_with(1)
```

**Run:** `python3 python/unittest_mock/example.py`

---

#### [Memory Management](./python/memory_management/)

Reference counting + cyclic GC in CPython.

```python
import gc, sys, weakref

obj = ["data"]
print(sys.getrefcount(obj))
weak = weakref.ref(obj)
del obj
print(weak() is None)  # True — object collected
gc.collect()
```

**Run:** `python3 python/memory_management/example.py`

---

## Run all examples

```bash
# Data structures
for d in linkedlist stack queues tree; do python3 $d/caller.py; done

# All Python interview topics
for d in python/*/; do python3 "${d}example.py"; done
```

---

## Project layout

```
python-datastructures/
├── README.md                 ← you are here
├── linkedlist/               # Singly linked list
├── stack/                    # LIFO stack
├── queues/                   # FIFO circular queue
├── tree/                     # Binary search tree
└── python/                   # 27 interview topics
    ├── decorator/
    ├── context_manager/
    ├── generator/
    ├── ... (22 more)
    └── README.md             # topic index
```

---

## Topic checklist (31 total)

| # | Topic | Folder |
|---|-------|--------|
| 1 | Linked List | [linkedlist/](./linkedlist/) |
| 2 | Stack | [stack/](./stack/) |
| 3 | Queue | [queues/](./queues/) |
| 4 | Binary Search Tree | [tree/](./tree/) |
| 5 | Decorators | [python/decorator/](./python/decorator/) |
| 6 | Context Managers | [python/context_manager/](./python/context_manager/) |
| 7 | Generators | [python/generator/](./python/generator/) |
| 8 | Iterators | [python/iterator/](./python/iterator/) |
| 9 | Closures | [python/closure/](./python/closure/) |
| 10 | *args & **kwargs | [python/args_kwargs/](./python/args_kwargs/) |
| 11 | Scope (LEGB) | [python/scope/](./python/scope/) |
| 12 | Comprehensions | [python/comprehension/](./python/comprehension/) |
| 13 | map / filter / zip | [python/lambda_map_filter/](./python/lambda_map_filter/) |
| 14 | Exception Handling | [python/exception_handling/](./python/exception_handling/) |
| 15 | Mutable Defaults | [python/mutable_default/](./python/mutable_default/) |
| 16 | is vs == | [python/identity_equality/](./python/identity_equality/) |
| 17 | Copy & Deepcopy | [python/copy_deepcopy/](./python/copy_deepcopy/) |
| 18 | Dunder Methods | [python/dunder_methods/](./python/dunder_methods/) |
| 19 | Inheritance & MRO | [python/inheritance_mro/](./python/inheritance_mro/) |
| 20 | Metaclasses | [python/metaclass/](./python/metaclass/) |
| 21 | Properties & Descriptors | [python/property_descriptor/](./python/property_descriptor/) |
| 22 | Dataclasses | [python/dataclass/](./python/dataclass/) |
| 23 | __slots__ | [python/slots/](./python/slots/) |
| 24 | Abstract Base Classes | [python/abc/](./python/abc/) |
| 25 | Threading & GIL | [python/threading/](./python/threading/) |
| 26 | Multiprocessing | [python/multiprocessing/](./python/multiprocessing/) |
| 27 | Async / Await | [python/async_await/](./python/async_await/) |
| 28 | functools | [python/functools_module/](./python/functools_module/) |
| 29 | Type Hints | [python/type_hints/](./python/type_hints/) |
| 30 | unittest.mock | [python/unittest_mock/](./python/unittest_mock/) |
| 31 | Memory Management | [python/memory_management/](./python/memory_management/) |
