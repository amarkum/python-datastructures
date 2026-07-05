"""Scope — LEGB rule, global, and nonlocal."""

x = "module-level"


def outer():
    x = "enclosing"

    def inner():
        nonlocal x
        x = "inner modified"
        print(f"    inner x: {x}")

    def reader():
        print(f"    reader x (enclosing): {x}")

    reader()
    inner()
    print(f"  outer x after inner: {x}")


def global_demo():
    global x
    print(f"  before global assign: {x}")
    x = "global modified"


def legb_demo():
    builtin_name = "local shadows nothing yet"
    print(f"  len is: {len}")  # Built-in
    print(f"  local: {builtin_name}")


counter = 0


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


if __name__ == "__main__":
    print("=== LEGB: Local, Enclosing, Global, Built-in ===")
    print(f"module x: {x}")
    outer()

    print("\n=== global ===")
    global_demo()
    print(f"module x after: {x}")

    print("\n=== legb_demo ===")
    legb_demo()

    print("\n=== factory with nonlocal ===")
    inc = make_counter()
    print(inc(), inc(), inc())
