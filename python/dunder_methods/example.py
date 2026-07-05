"""Dunder (magic) methods — operator overloading and protocols."""


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        return 2

    def __getitem__(self, index):
        return (self.x, self.y)[index]


class Stack(list):
    """Minimal stack using dunder methods."""

    def __repr__(self):
        return f"Stack({list(self)})"

    def push(self, item):
        self.append(item)

    def pop_item(self):
        if not self:
            raise IndexError("pop from empty stack")
        return self.pop()


class Sentence:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.text.split())


if __name__ == "__main__":
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print("=== Vector ===")
    print(v1 + v2)
    print(v1 == v2)
    print(v1[0])

    print("\n=== Stack ===")
    s = Stack()
    s.push(1)
    s.push(2)
    print(s)
    print(s.pop_item())

    print("\n=== __str__ vs __repr__ ===")
    sent = Sentence("hello world")
    print(str(sent), len(sent))
