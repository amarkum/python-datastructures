"""Generator examples — lazy iteration with yield."""


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def read_large_file_lines(path):
    """Memory-efficient line-by-line reading."""
    with open(path) as f:
        for line in f:
            yield line.rstrip("\n")


def send_example():
    """Demonstrate two-way communication via .send()."""
    total = 0
    while True:
        value = yield total
        if value is None:
            break
        total += value


if __name__ == "__main__":
    print("=== countdown ===")
    for i in countdown(5):
        print(i, end=" ")
    print()

    print("\n=== fibonacci (< 100) ===")
    print(list(fibonacci(100)))

    print("\n=== generator expression vs list comprehension ===")
    gen = (x * x for x in range(1_000_000))  # lazy — no list in memory
    print(f"First 5 squares: {[next(gen) for _ in range(5)]}")

    print("\n=== .send() ===")
    gen = send_example()
    next(gen)  # prime the generator
    print(gen.send(10))  # 10
    print(gen.send(20))  # 30
