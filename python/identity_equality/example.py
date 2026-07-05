"""Identity vs equality — is, ==, hashable, and immutable types."""

a = [1, 2, 3]
b = [1, 2, 3]
c = a

small_a = 256
small_b = 256
large_a = 257
large_b = 257


class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name


class HashablePerson:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, HashablePerson) and self.name == other.name

    def __hash__(self):
        return hash(self.name)


if __name__ == "__main__":
    print("=== == vs is ===")
    print(f"a == b: {a == b}")
    print(f"a is b: {a is b}")
    print(f"a is c: {a is c}")

    print("\n=== Integer interning (implementation detail) ===")
    print(f"small 256 is: {small_a is small_b}")
    print(f"large 257 is: {large_a is large_b}")

    print("\n=== None, True, False — always use is ===")
    value = None
    print(value is None)

    print("\n=== Hashable vs unhashable ===")
    try:
        {a: "list key"}
    except TypeError as e:
        print(f"  list not hashable: {e}")

    p = HashablePerson("Alice")
    print(f"  set of HashablePerson: {{{p}}}")

    print("\n=== Custom __eq__ without __hash__ ===")
    p1, p2 = Person("Bob"), Person("Bob")
    print(f"  equal: {p1 == p2}, same id: {p1 is p2}")
