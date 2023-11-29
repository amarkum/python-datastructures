class Stack:
    def __init__(self, capacity):
        """
        Initializes the Stack with a specified capacity.
        :param capacity: The maximum size of the stack.
        """
        self.max_size = capacity
        self.top = -1
        self.arr = [None] * self.max_size

    def is_empty(self):
        """
        Checks if the stack is empty.
        :return: True if the stack is empty, False otherwise.
        """
        return self.top == -1

    def is_full(self):
        """
        Checks if the stack is full.
        :return: True if the stack is full, False otherwise.
        """
        return self.top == self.max_size - 1

    def get_top(self):
        """
        Returns the top element of the stack.
        :return: The top element of the stack, or None if the stack is empty.
        """
        if self.is_empty():
            return None
        return self.arr[self.top]

    def push(self, value):
        """
        Adds an element to the top of the stack.
        :param value: The value to be added.
        """
        if self.is_full():
            print("Stack is Full")
            return
        self.top += 1
        self.arr[self.top] = value

    def pop(self):
        """
        Removes and returns the top element of the stack.
        :return: The element at the top of the stack.
        """
        if self.is_empty():
            print("Stack is Empty")
            return None
        value = self.arr[self.top]
        self.top -= 1
        return value
