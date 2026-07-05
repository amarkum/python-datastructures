# python-datastructures

Master data structures and Python interview concepts in Python.

## Project structure

```
python-datastructures/
├── linkedlist/       # Singly linked list
├── stack/            # Array-based stack (LIFO)
├── queues/           # Circular queue (FIFO)
├── tree/             # Binary search tree
└── python/           # Python interview topics (25 modules)
```

## Data structures

| Folder | Description | Run demo |
|--------|-------------|----------|
| [linkedlist](./linkedlist/) | Singly linked list with reversal, loop detection | `python3 linkedlist/caller.py` |
| [stack](./stack/) | Fixed-capacity stack | `python3 stack/caller.py` |
| [queues](./queues/) | Circular queue | `python3 queues/caller.py` |
| [tree](./tree/) | Binary search tree | `python3 tree/caller.py` |

## Python interview topics

Full index: [python/README.md](./python/README.md)

### Core language

| Topic | Folder |
|-------|--------|
| Decorators | [python/decorator](./python/decorator/) |
| Context managers | [python/context_manager](./python/context_manager/) |
| Generators | [python/generator](./python/generator/) |
| Iterators | [python/iterator](./python/iterator/) |
| Closures | [python/closure](./python/closure/) |
| *args & **kwargs | [python/args_kwargs](./python/args_kwargs/) |
| Scope (LEGB) | [python/scope](./python/scope/) |
| Comprehensions | [python/comprehension](./python/comprehension/) |
| map, filter, zip | [python/lambda_map_filter](./python/lambda_map_filter/) |
| Exception handling | [python/exception_handling](./python/exception_handling/) |
| Mutable default args | [python/mutable_default](./python/mutable_default/) |
| is vs == | [python/identity_equality](./python/identity_equality/) |
| Copy & deepcopy | [python/copy_deepcopy](./python/copy_deepcopy/) |

### OOP & classes

| Topic | Folder |
|-------|--------|
| Dunder methods | [python/dunder_methods](./python/dunder_methods/) |
| Inheritance & MRO | [python/inheritance_mro](./python/inheritance_mro/) |
| Metaclasses | [python/metaclass](./python/metaclass/) |
| Properties & descriptors | [python/property_descriptor](./python/property_descriptor/) |
| Dataclasses | [python/dataclass](./python/dataclass/) |
| __slots__ | [python/slots](./python/slots/) |
| Abstract base classes | [python/abc](./python/abc/) |

### Concurrency & async

| Topic | Folder |
|-------|--------|
| Threading & GIL | [python/threading](./python/threading/) |
| Multiprocessing | [python/multiprocessing](./python/multiprocessing/) |
| Async / await | [python/async_await](./python/async_await/) |

### Standard library & tooling

| Topic | Folder |
|-------|--------|
| functools | [python/functools_module](./python/functools_module/) |
| Type hints | [python/type_hints](./python/type_hints/) |
| unittest.mock | [python/unittest_mock](./python/unittest_mock/) |
| Memory management | [python/memory_management](./python/memory_management/) |

### Quick start

```bash
cd python/decorator && python3 example.py
```

## Requirements

- Python 3.8+

No external dependencies required.
