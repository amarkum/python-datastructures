class Queue:
    def __init__(self, capacity):
        """
        Initializes the Queue with a specified capacity.
        :param capacity: The maximum size of the queue.
        """
        self.array = [None] * capacity
        self.max_size = capacity
        self.front = 0
        self.back = -1
        self.current_size = 0

    def is_empty(self):
        """
        Checks if the queue is empty.
        :return: True if the queue is empty, False otherwise.
        """
        return self.current_size == 0

    def get_current_size(self):
        """
        Gets the current size of the queue.
        :return: The number of elements in the queue.
        """
        return self.current_size

    def is_full(self):
        """
        Checks if the queue is full.
        :return: True if the queue is full, False otherwise.
        """
        return self.current_size == self.max_size

    def enqueue(self, value):
        """
        Adds an element to the back of the queue.
        :param value: The value to be added.
        """
        if self.is_full():
            print("Queue Full")
            return
        self.back = (self.back + 1) % self.max_size
        self.array[self.back] = value
        self.current_size += 1

    def dequeue(self):
        """
        Removes and returns the front element of the queue.
        :return: The element at the front of the queue.
        """
        if self.is_empty():
            print("Queue is Empty")
            return None
        value = self.array[self.front]
        self.front = (self.front + 1) % self.max_size
        self.current_size -= 1
        return value
