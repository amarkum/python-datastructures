# Python Binary Search Tree Implementation

## Overview

This project provides a Python implementation of a Binary Search Tree (BST), a fundamental data structure used in computer science. The BST allows for fast lookup, addition, and deletion of items and maintains its elements in a sorted order.

## Features

- **Add Elements**: Efficiently add elements to the tree while maintaining order.
- **Search Elements**: Quickly search for elements in the tree.
- **Print Tree**: Print the tree structure in a readable format.
- **Find Height**: Determine the height of the tree.
- **Delete Elements**: Remove elements from the tree.

## Installation

No additional installation is required. Ensure you have Python installed on your system.

## Usage

To use the `BinarySearchTree` class, import it into your Python script. Here's a quick example:

```python
from binary_search_tree import BinarySearchTree

# Create a new instance of BinarySearchTree
bst = BinarySearchTree()

# Add elements
bst.add(5)
bst.add(3)
bst.add(7)
bst.add(1)
bst.add(9)

# Search for an element
print("Search for 3:", "Found" if bst.search(3) else "Not found")

# Print the tree
print("Binary Search Tree:")
bst.print_tree(bst.root)
