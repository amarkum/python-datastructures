"""Memory management — reference counting, gc, and weakref."""

import gc
import sys
import weakref


class Node:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"  __del__ called for {self.name}")


def ref_count_demo():
    obj = Node("alpha")
    print(f"  refcount: {sys.getrefcount(obj) - 1}")  # adjust for getrefcount arg
    ref = obj
    print(f"  after alias: {sys.getrefcount(obj) - 1}")
    del ref
    del obj


def cyclic_demo():
    a = Node("A")
    b = Node("B")
    a.partner = b
    b.partner = a
    del a, b
    collected = gc.collect()
    print(f"  gc collected {collected} objects")


def weakref_demo():
    obj = ["data"]
    weak = weakref.ref(obj)
    print(f"  weak ref alive: {weak() is not None}")
    del obj
    print(f"  weak ref dead: {weak() is None}")


if __name__ == "__main__":
    print("=== Reference counting ===")
    ref_count_demo()

    print("\n=== Cyclic references + gc ===")
    cyclic_demo()

    print("\n=== weakref ===")
    weakref_demo()

    print("\n=== gc stats ===")
    print(f"  gc enabled: {gc.isenabled()}")
    print(f"  tracked objects: {len(gc.get_objects()):,}")
