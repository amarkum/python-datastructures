
# Python Stack Implementation

## Overview

This project provides a Python implementation of a Stack, a fundamental data structure that follows the Last In First Out (LIFO) principle. The last element added to the stack will be the first one to be removed.

## Features

- **Push**: Add elements to the top of the stack.
- **Pop**: Remove elements from the top of the stack.
- **Check Full**: Determine if the stack is full.
- **Check Empty**: Determine if the stack is empty.
- **Get Top Element**: View the top element of the stack.

## Installation

No additional installation is required. Ensure you have Python installed on your system.

## Usage

Here's a quick example of how to use the `Stack` class:

```python
from stack_custom import Stack

# Create a new instance of Stack with a specific capacity
stack = Stack(5)

# Push elements onto the stack
for i in range(5):
    stack.push(i)

# Pop and display elements
while not stack.is_empty():
    print(stack.pop())
