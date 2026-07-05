# Python Interview Topics

Commonly asked Python concepts for software engineer interviews. Each folder contains a runnable `example.py` and a `README.md`.

## Core language

| Folder | Concept | Run |
|--------|---------|-----|
| [decorator](./decorator/) | Function/class decorators | `python3 example.py` |
| [context_manager](./context_manager/) | `with` statement | `python3 example.py` |
| [generator](./generator/) | Generators & `yield` | `python3 example.py` |
| [iterator](./iterator/) | Iterator protocol | `python3 example.py` |
| [closure](./closure/) | Closures & nested functions | `python3 example.py` |
| [args_kwargs](./args_kwargs/) | `*args` & `**kwargs` | `python3 example.py` |
| [scope](./scope/) | LEGB, `global`, `nonlocal` | `python3 example.py` |
| [comprehension](./comprehension/) | List/dict/set comprehensions | `python3 example.py` |
| [lambda_map_filter](./lambda_map_filter/) | `map`, `filter`, `zip` | `python3 example.py` |
| [exception_handling](./exception_handling/) | try/except/else/finally | `python3 example.py` |
| [mutable_default](./mutable_default/) | Mutable default argument trap | `python3 example.py` |
| [identity_equality](./identity_equality/) | `is` vs `==`, hashability | `python3 example.py` |
| [copy_deepcopy](./copy_deepcopy/) | Shallow vs deep copy | `python3 example.py` |

## OOP & classes

| Folder | Concept | Run |
|--------|---------|-----|
| [dunder_methods](./dunder_methods/) | Magic methods | `python3 example.py` |
| [inheritance_mro](./inheritance_mro/) | Inheritance & MRO | `python3 example.py` |
| [metaclass](./metaclass/) | Metaclasses | `python3 example.py` |
| [property_descriptor](./property_descriptor/) | Properties & descriptors | `python3 example.py` |
| [dataclass](./dataclass/) | `@dataclass` | `python3 example.py` |
| [slots](./slots/) | `__slots__` | `python3 example.py` |
| [abc](./abc/) | Abstract base classes | `python3 example.py` |

## Concurrency & async

| Folder | Concept | Run |
|--------|---------|-----|
| [threading](./threading/) | Threads, locks, GIL | `python3 example.py` |
| [multiprocessing](./multiprocessing/) | Processes & CPU parallelism | `python3 example.py` |
| [async_await](./async_await/) | Async I/O | `python3 example.py` |

## Standard library & tooling

| Folder | Concept | Run |
|--------|---------|-----|
| [functools_module](./functools_module/) | `lru_cache`, `partial` | `python3 example.py` |
| [type_hints](./type_hints/) | Typing & generics | `python3 example.py` |
| [unittest_mock](./unittest_mock/) | Mocking & patching | `python3 example.py` |
| [memory_management](./memory_management/) | GC, refcount, weakref | `python3 example.py` |

## How to use

```bash
cd python/<topic>
python3 example.py
```

Read the README in each folder for theory, interview questions, and a walkthrough of `example.py`.
