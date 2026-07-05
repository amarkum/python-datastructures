# Binary Search Tree

A binary search tree (BST) implementation with insert, search, delete, and height operations.

## Files

| File | Description |
|------|-------------|
| `binarysearchtreecustom.py` | Core `Node` and `BinarySearchTree` classes |
| `caller.py` | Demo script |

---

## binarysearchtreecustom.py

### Classes

**`Node`** — Tree node with `data`, `left`, and `right` pointers.

**`BinarySearchTree`**

| Method | Description | Average time |
|--------|-------------|--------------|
| `add(value)` | Insert a value | O(log n) |
| `search(value)` | Find a value | O(log n) |
| `delete(value)` | Remove a node | O(log n) |
| `find_height(node)` | Compute tree height | O(n) |
| `print_tree(node)` | Print tree sideways (root on left) | O(n) |
| `is_empty()` | Check if tree is empty | O(1) |

Deletion handles three cases: no children, one child, and two children (inorder successor).

### Usage

```python
from binarysearchtreecustom import BinarySearchTree

bst = BinarySearchTree()
bst.add(5)
bst.add(3)
print(bst.search(3))  # True
bst.print_tree(bst.root)
```

---

## caller.py

### Class: `BinarySearchTreeCaller`

| Method | Description |
|--------|-------------|
| `main()` | Builds a BST, searches, prints, deletes a node, prints height |

### Run

```bash
python3 caller.py
```
