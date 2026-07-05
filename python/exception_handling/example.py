"""Exception handling — try/except, else, finally, custom exceptions."""


class ValidationError(Exception):
    """Raised when input validation fails."""

    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def parse_age(value):
    try:
        age = int(value)
    except ValueError as e:
        raise ValidationError("age", f"must be an integer, got {value!r}") from e

    if age < 0 or age > 150:
        raise ValidationError("age", "must be between 0 and 150")
    return age


def read_config(path):
    """Demonstrate try/except/else/finally."""
    file = None
    try:
        file = open(path)
    except FileNotFoundError:
        print(f"  Config not found: {path}")
        return {}
    else:
        print(f"  Loaded config from {path}")
        return {"status": "ok"}
    finally:
        if file:
            file.close()
            print("  File closed")


class Resource:
    def __enter__(self):
        print("  Resource acquired")
        return self

    def __exit__(self, *args):
        print("  Resource released")


if __name__ == "__main__":
    print("=== Basic try/except ===")
    try:
        print(divide(10, 2))
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"  Caught: {e}")

    print("\n=== Chained exceptions ===")
    try:
        parse_age("not-a-number")
    except ValidationError as e:
        print(f"  {e}")
        print(f"  Cause: {e.__cause__}")

    print("\n=== else / finally ===")
    read_config("/tmp/nonexistent_config.txt")

    print("\n=== Context manager cleanup ===")
    with Resource():
        print("  Using resource")
