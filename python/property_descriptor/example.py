"""Property and descriptor examples."""

from typing import Any


class Celsius:
    """Descriptor that stores temperature in Celsius."""

    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name, 0.0)

    def __set__(self, obj, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        obj.__dict__[self.name] = float(value)


class Temperature:
    celsius = Celsius("celsius")

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self):
        return 3.14159 * self._radius ** 2


class ValidatedAttribute:
    """Reusable descriptor with validation."""

    def __init__(self, validator):
        self.validator = validator
        self.name = ""

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        self.validator(value)
        obj.__dict__[self.name] = value


def positive_number(value):
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError("Must be a positive number")


class Product:
    price = ValidatedAttribute(positive_number)


if __name__ == "__main__":
    print("=== @property ===")
    c = Circle(5)
    print(f"radius={c.radius}, area={c.area:.2f}")
    c.radius = 10
    print(f"radius={c.radius}, area={c.area:.2f}")

    print("\n=== Descriptor + property ===")
    t = Temperature()
    t.celsius = 25
    print(f"25°C = {t.fahrenheit:.1f}°F")
    t.fahrenheit = 32
    print(f"32°F = {t.celsius:.1f}°C")

    print("\n=== Validated descriptor ===")
    p = Product()
    p.price = 19.99
    print(f"Price: ${p.price}")
