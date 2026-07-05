"""Inheritance and MRO — super(), multiple inheritance, method resolution order."""

class Animal:
    def speak(self):
        return "..."


class Flyer:
    def move(self):
        return "flying"


class Swimmer:
    def move(self):
        return "swimming"


class Duck(Animal, Flyer, Swimmer):
    def speak(self):
        return "quack"

    def move(self):
        return super().move()


class A:
    def greet(self):
        return "A"


class B(A):
    def greet(self):
        return f"B -> {super().greet()}"


class C(A):
    def greet(self):
        return f"C -> {super().greet()}"


class D(B, C):
    def greet(self):
        return f"D -> {super().greet()}"


if __name__ == "__main__":
    print("=== MRO ===")
    print(D.__mro__)
    print(D().greet())

    print("\n=== Duck — super picks Flyer.move (left-to-right MRO) ===")
    d = Duck()
    print(d.speak(), d.move())

    print("\n=== isinstance / issubclass ===")
    print(isinstance(d, Animal), issubclass(Duck, Flyer))
