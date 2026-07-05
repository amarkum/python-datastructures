"""Closure examples — functions that capture enclosing scope."""


def make_multiplier(factor):
    def multiply(x):
        return x * factor  # `factor` is captured from enclosing scope

    return multiply


def make_counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count
        count += step
        return count

    def get_count():
        return count

    return increment, get_count


# Classic interview trap: late binding in loops
def make_multipliers_wrong():
    return [lambda x: i * x for i in range(5)]


def make_multipliers_correct():
    return [lambda x, i=i: i * x for i in range(5)]


if __name__ == "__main__":
    print("=== Basic closure ===")
    double = make_multiplier(2)
    triple = make_multiplier(3)
    print(double(10), triple(10))

    print("\n=== nonlocal ===")
    inc, get = make_counter(100)
    print(inc(), inc(), get())

    print("\n=== Late binding trap ===")
    wrong = make_multipliers_wrong()
    print("Wrong [0]:", wrong[0](10))  # all use i=4
    correct = make_multipliers_correct()
    print("Correct [0]:", correct[0](10))
