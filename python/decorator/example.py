"""Decorator examples — common Python interview topic."""

import functools
import time


# --- Basic decorator ---
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result

    return wrapper


@timer
def slow_add(a, b):
    time.sleep(0.1)
    return a + b


# --- Decorator with arguments ---
def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)
def greet(name):
    print(f"Hello, {name}!")


# --- Class-based decorator ---
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Call #{self.calls} to {self.func.__name__}")
        return self.func(*args, **kwargs)


@CountCalls
def square(n):
    return n * n


if __name__ == "__main__":
    print("=== Basic decorator ===")
    print(slow_add(2, 3))

    print("\n=== Parameterized decorator ===")
    greet("Python")

    print("\n=== Class decorator ===")
    print(square(5))
    print(square(5))
