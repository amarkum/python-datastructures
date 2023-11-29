# Linked List Quick Reference Guide

## Overview

A linked list is a linear data structure where each element is a separate object, called a node. Each node contains the data and a reference to the next node in the list.

## Types of Linked Lists

- **Singly Linked List**: Each node has a single reference to the next node.
- **Doubly Linked List**: Each node has two references, one to the next node and another to the previous node.
- **Circular Linked List**: The last node points back to the first node, making a circle.

## Key Operations

1. **Addition**
   - `add_at_head(data)`: Add a node with `data` at the beginning.
   - `add_at_end(data)`: Add a node with `data` at the end.

2. **Deletion**
   - `delete_at_head()`: Remove the first node.
   - `delete_by_value(value)`: Remove a node with the specified `value`.

3. **Traversal**
   - `print_all()`: Print all elements of the list.

4. **Reversal**
   - `reverse()`: Reverse the linked list in place.

5. **Searching**
   - `find_mid()`: Find the middle element of the list.

6. **Loop Detection**
   - `detect_loop()`: Detect if there's a loop in the list.

## Example Implementation in Python

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Constructor and other methods...
