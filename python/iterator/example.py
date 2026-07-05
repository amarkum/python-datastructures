"""Iterator protocol — __iter__ and __next__."""


class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class BatchIterator:
    """Yield items from an iterable in fixed-size chunks."""

    def __init__(self, iterable, batch_size):
        self._iterator = iter(iterable)
        self.batch_size = batch_size

    def __iter__(self):
        return self

    def __next__(self):
        batch = []
        try:
            for _ in range(self.batch_size):
                batch.append(next(self._iterator))
        except StopIteration:
            if not batch:
                raise
        return batch


if __name__ == "__main__":
    print("=== CountDown iterator ===")
    for n in CountDown(5):
        print(n, end=" ")
    print()

    print("\n=== BatchIterator ===")
    data = list(range(10))
    for batch in BatchIterator(data, 3):
        print(batch)

    print("\n=== Built-in iter tools ===")
    it = iter([1, 2, 3])
    print(list(it))
