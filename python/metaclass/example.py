"""Metaclass basics — classes that create classes."""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=SingletonMeta):
    def __init__(self, connection_string):
        self.connection_string = connection_string


class ValidatedMeta(type):
    """Reject classes that don't define required attributes."""

    required = ("name", "version")

    def __new__(mcs, name, bases, namespace):
        for attr in mcs.required:
            if attr not in namespace:
                raise TypeError(f"{name} must define '{attr}'")
        return super().__new__(mcs, name, bases, namespace)


class Plugin(metaclass=ValidatedMeta):
    name = "example"
    version = "1.0"


if __name__ == "__main__":
    print("=== Singleton metaclass ===")
    db1 = Database("postgres://localhost")
    db2 = Database("mysql://other")
    print(f"Same instance: {db1 is db2}")
    print(f"Connection: {db1.connection_string}")

    print("\n=== Validated metaclass ===")
    print(f"Plugin: {Plugin.name} v{Plugin.version}")

    print("\n=== type() creates classes dynamically ===")
    Dynamic = type("Dynamic", (), {"x": 42})
    print(f"Dynamic().x = {Dynamic().x}")
