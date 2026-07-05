"""Mutable default argument — classic Python interview trap."""


def append_bad(item, target=[]):
    target.append(item)
    return target


def append_good(item, target=None):
    if target is None:
        target = []
    target.append(item)
    return target


def create_multipliers_wrong():
    return [lambda x: i * x for i in range(4)]


def create_multipliers_good():
    return [lambda x, i=i: i * x for i in range(4)]


if __name__ == "__main__":
    print("=== Mutable default trap ===")
    print(append_bad(1))
    print(append_bad(2))  # surprise: [1, 2] not [2]!
    print(f"  shared default id: same list reused")

    print("\n=== Fixed with None sentinel ===")
    print(append_good(1))
    print(append_good(2))  # [2] as expected

    print("\n=== Same trap in class attributes ===")
    print("  Use dataclass field(default_factory=list) or __init__ assignment")

    print("\n=== Late binding in lambdas (related trap) ===")
    wrong = create_multipliers_wrong()
    good = create_multipliers_good()
    print(f"  wrong[0](10) = {wrong[0](10)}  (expected 0, got 30)")
    print(f"  good[0](10) = {good[0](10)}")
