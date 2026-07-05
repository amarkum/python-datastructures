"""__slots__ — memory-efficient classes with fixed attributes."""

class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointWithSlots:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


class ChildWithExtraSlot(PointWithSlots):
    __slots__ = ("z",)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


if __name__ == "__main__":
    p1 = PointWithoutSlots(1, 2)
    p2 = PointWithSlots(3, 4)
    p3 = ChildWithExtraSlot(1, 2, 3)

    print("=== Instances ===")
    print(p1.x, p2.x, p3.z)

    print("\n=== No __dict__ on slotted class ===")
    print(hasattr(p1, "__dict__"), hasattr(p2, "__dict__"))

    print("\n=== Cannot add arbitrary attributes ===")
    try:
        p2.label = "origin"
    except AttributeError as e:
        print(f"  AttributeError: {e}")

    print("\n=== __slots__ saves memory for many instances ===")
    import sys
    print(f"  PointWithoutSlots instance: ~{sys.getsizeof(p1.__dict__)} bytes (__dict__ alone)")
