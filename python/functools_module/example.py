"""functools — lru_cache, partial, reduce, and wraps."""

import functools
from operator import add


@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def multiply(a, b, c):
    return a * b * c


def pipeline(*functions):
    def run(value):
        for func in functions:
            value = func(value)
        return value

    return run


if __name__ == "__main__":
    print("=== lru_cache ===")
    print(fibonacci(30))
    print(fibonacci.cache_info())

    print("\n=== partial ===")
    double = functools.partial(multiply, 2)
    print(double(5, 3))

    print("\n=== reduce ===")
    print(functools.reduce(add, [1, 2, 3, 4, 5]))

    print("\n=== pipeline ===")
    process = pipeline(str.strip, str.upper)
    print(process("  hello  "))

    print("\n=== cache_clear ===")
    fibonacci.cache_clear()
    print("Cache cleared")
