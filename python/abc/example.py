"""Abstract Base Classes — enforce interfaces with abc module."""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class InvalidShape(Shape):
    pass  # missing abstract methods


class Storage(ABC):
    @abstractmethod
    def save(self, data):
        pass

    @abstractmethod
    def load(self, key):
        pass


class MemoryStorage(Storage):
    def __init__(self):
        self._data = {}

    def save(self, data):
        key = str(len(self._data))
        self._data[key] = data
        return key

    def load(self, key):
        return self._data[key]


if __name__ == "__main__":
    print("=== Valid implementation ===")
    rect = Rectangle(4, 5)
    print(f"area={rect.area()}, perimeter={rect.perimeter()}")

    print("\n=== Cannot instantiate ABC directly ===")
    try:
        Shape()
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\n=== Incomplete subclass fails at instantiation ===")
    try:
        InvalidShape()
    except TypeError as e:
        print(f"  TypeError: {e}")

    print("\n=== Storage interface ===")
    store = MemoryStorage()
    key = store.save({"name": "Alice"})
    print(store.load(key))
