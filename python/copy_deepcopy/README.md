# Copy & Deepcopy

Assignment creates an alias. `copy.copy()` is shallow. `copy.deepcopy()` is fully independent.

## Files

| File | Description |
|------|-------------|
| `example.py` | Shallow vs deep, assignment, cyclic structures |

---

## Descriptive Example

### Scenario

Copy a nested list — shallow copy shares inner lists, deep copy does not.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0].append(99)

print(original)   # [[1, 2, 99], [3, 4]]
print(shallow)    # [[1, 2, 99], [3, 4]]  ← inner list shared!
print(deep)       # [[1, 2], [3, 4]]      ← unaffected
```

### Assignment vs copy

```python
a = [1, 2, 3]
alias = a           # same object
copied = a.copy()   # new outer list

a.append(4)
print(alias)    # [1, 2, 3, 4] — alias sees change
print(copied)   # [1, 2, 3]    — independent
```

---

## Interview Q&A

**Q1: What is the difference between shallow and deep copy?**  
A: Shallow copy creates a new outer container but inner objects are shared. Deep copy recursively copies everything into fully independent objects.

**Q2: When do you need deepcopy?**  
A: When you need complete independence — nested mutables, graphs, or when downstream code might mutate nested structures.

**Q3: Does `list.copy()` perform a deep copy?**  
A: No. `list.copy()` and `copy.copy()` are both shallow. Use `copy.deepcopy()` for nested independence.

**Q4: What about copying objects with circular references?**  
A: `deepcopy` handles cycles by tracking already-copied objects. Manual recursion would infinite-loop without this.

**Q5: Copy vs pickle for cloning objects?**  
A: Pickle serializes/deserializes — also creates a copy but slower and has security implications with untrusted data.

**Q6: When is shallow copy sufficient?**  
A: Flat lists, immutable contents, or when you intentionally want shared inner objects (e.g., shared config reference).

---

## Run

```bash
python3 example.py
```
