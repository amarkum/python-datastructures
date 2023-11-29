# Python Queue Implementation

## Overview

This project implements a basic queue data structure in Python. A queue is a linear data structure that follows the First In First Out (FIFO) principle, where the first element added to the queue will be the first one to be removed.

## Features

- **Enqueue**: Add elements to the back of the queue.
- **Dequeue**: Remove elements from the front of the queue.
- **Check Full**: Determine if the queue is full.
- **Check Empty**: Determine if the queue is empty.
- **Get Current Size**: Get the number of elements in the queue.

## Installation

No additional installation is required. Ensure you have Python installed on your system.

## Usage

Here's a simple example of how to use the `Queue` class:

```python
from queue_custom import Queue

# Create a new instance of Queue with a specific capacity
queue = Queue(5)

# Enqueue elements
for i in range(5):
    queue.enqueue(i)

# Dequeue and display elements
while not queue.is_empty():
    print(queue.dequeue())
