"""lambda, map, filter, zip — functional-style Python."""

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6, 7, 8]

if __name__ == "__main__":
    print("=== lambda ===")
    square = lambda x: x ** 2
    print(list(map(square, numbers[:4])))

    print("\n=== map ===")
    doubled = list(map(lambda x: x * 2, numbers))
    print(doubled)

    print("\n=== filter ===")
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(evens)

    print("\n=== reduce ===")
    total = reduce(lambda acc, x: acc + x, numbers)
    print(total)

    print("\n=== zip ===")
    names = ["Alice", "Bob", "Carol"]
    scores = [90, 85, 88]
    for name, score in zip(names, scores):
        print(f"  {name}: {score}")

    print("\n=== enumerate ===")
    for i, val in enumerate(numbers[:3], start=1):
        print(f"  {i}. {val}")

    print("\n=== sorted with key ===")
    words = ["banana", "pie", "Washington", "book"]
    print(sorted(words, key=lambda w: w.lower()))
