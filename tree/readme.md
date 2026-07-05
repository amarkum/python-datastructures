# Binary Search Tree

Ordered binary tree — left subtree values are smaller, right subtree values are larger. Supports O(log n) search, insert, and delete on average.

## Files

| File | Description |
|------|-------------|
| `binarysearchtreecustom.py` | `Node` and `BinarySearchTree` |
| `caller.py` | Build, search, delete, height demo |

---

## Descriptive Example

### Scenario

Insert values, search for one present and one absent, delete a node with two children, print the tree.

```python
from binarysearchtreecustom import BinarySearchTree

bst = BinarySearchTree()
for v in [6, 4, 9, 5, 2, 8, 12]:
    bst.add(v)

print(bst.search(12))   # True
print(bst.search(108))  # False

bst.delete(9)           # node with two children → replaced by inorder successor
bst.print_tree(bst.root)
print(bst.find_height(bst.root))
```

### Delete cases

1. **No children** — remove node, set parent pointer to `None`
2. **One child** — replace node with its child
3. **Two children** — copy inorder successor (min of right subtree) into node, delete successor

---

## Interview Q&A

**Q1: What is the time complexity of BST operations?**  
A: Average O(log n) for balanced trees. Worst O(n) if tree degenerates to a linked list (sorted insert order).

**Q2: How is a BST different from a binary heap?**  
A: BST maintains sorted order (left < node < right). Heap maintains heap property for min/max extraction, not full sorting.

**Q3: What is an inorder traversal of a BST?**  
A: Left → Node → Right. Produces values in sorted ascending order.

**Q4: How do you delete a node with two children?**  
A: Find inorder successor (smallest in right subtree) or predecessor (largest in left), copy its value, delete that node.

**Q5: How do you balance a BST?**  
A: Use self-balancing variants: AVL tree (strict balance), Red-Black tree (relaxed balance), or rebuild from sorted array.

**Q6: BST vs hash table for lookup?**  
A: Hash table: O(1) average, no ordering. BST: O(log n), supports range queries, ordered traversal, predecessor/successor.

---

## Run

```bash
python3 caller.py
```
