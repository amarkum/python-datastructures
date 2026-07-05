# Dataclasses

Auto-generate boilerplate (`__init__`, `__repr__`, `__eq__`) for data-holding classes.

## Files

| File | Description |
|------|-------------|
| `example.py` | Basic, frozen, and `default_factory` dataclasses |

---

## Descriptive Example

### Scenario

Model a team with a name and a list of members — safely handle mutable defaults.

```python
from dataclasses import dataclass, field, replace

@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)

    def add(self, member):
        self.members.append(member)

t1 = Team("Alpha")
t2 = Team("Beta")
t1.add("Alice")

print(t1)   # Team(name='Alpha', members=['Alice'])
print(t2)   # Team(name='Beta', members=[])  — independent list!
```

### Immutable dataclass

```python
@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float

p = Point(1.0, 2.0)
# p.x = 5        # FrozenInstanceError
print(Point(1, 2) < Point(3, 4))   # True (order=True)
```

---

## Interview Q&A

**Q1: What does `@dataclass` auto-generate?**  
A: `__init__`, `__repr__`, and optionally `__eq__`, `__order__`, `__hash__` depending on parameters.

**Q2: Dataclass vs NamedTuple?**  
A: Dataclass: mutable by default (unless frozen), regular class. NamedTuple: immutable, tuple subclass, lighter weight.

**Q3: Why `field(default_factory=list)` instead of `members=[]`?**  
A: Mutable default trap — `[]` is shared across instances. `default_factory` calls `list()` per instance.

**Q4: What does `frozen=True` do?**  
A: Makes instances immutable. Enables hashing (if all fields hashable). Raises `FrozenInstanceError` on attribute assignment.

**Q5: Dataclass vs dict for data?**  
A: Dataclass: type safety, IDE autocomplete, validation hooks, immutability option. Dict: flexible keys, JSON-native, no schema.

**Q6: Can dataclasses use `__slots__`?**  
A: Yes — `@dataclass(slots=True)` in Python 3.10+ combines both features.

---

## Run

```bash
python3 example.py
```
