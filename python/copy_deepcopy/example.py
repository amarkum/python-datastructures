"""Shallow vs deep copy — aliasing and nested mutability."""

import copy


def show(label, obj):
    print(f"  {label}: {obj}")


if __name__ == "__main__":
    original = [[1, 2], [3, 4]]
    shallow = copy.copy(original)
    deep = copy.deepcopy(original)

    print("=== Before mutation ===")
    show("original", original)
    show("shallow", shallow)
    show("deep", deep)

    print("\n=== Mutate nested list in original ===")
    original[0].append(99)

    show("original", original)
    show("shallow (affected!)", shallow)
    show("deep (unchanged)", deep)

    print("\n=== Assignment vs copy ===")
    a = [1, 2, 3]
    alias = a
    copied = a.copy()
    a.append(4)
    print(f"  alias: {alias}")
    print(f"  copied: {copied}")

    print("\n=== deepcopy breaks cycles ===")
    cyclic = []
    cyclic.append(cyclic)
    cloned = copy.deepcopy(cyclic)
    print(f"  cyclic is cloned[0]: {cloned is cloned[0]}")
