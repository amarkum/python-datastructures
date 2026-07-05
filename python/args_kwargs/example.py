"""*args and **kwargs — flexible function signatures and unpacking."""

def log_call(func_name, *args, **kwargs):
    print(f"  {func_name}(args={args}, kwargs={kwargs})")


def sum_all(*args):
    return sum(args)


def build_profile(name, **kwargs):
    profile = {"name": name}
    profile.update(kwargs)
    return profile


def wrapper(func, *args, **kwargs):
    log_call(func.__name__, *args, **kwargs)
    return func(*args, **kwargs)


def greet(greeting, name, punctuation="!"):
    return f"{greeting}, {name}{punctuation}"


if __name__ == "__main__":
    print("=== *args ===")
    print(sum_all(1, 2, 3, 4))

    print("\n=== **kwargs ===")
    print(build_profile("Alice", role="engineer", city="NYC"))

    print("\n=== Unpacking with * and ** ===")
    args = ("Hello", "Bob")
    kwargs = {"punctuation": "?"}
    print(greet(*args, **kwargs))

    print("\n=== Forwarding args/kwargs ===")
    print(wrapper(greet, "Hi", "Python"))

    print("\n=== Merge dicts (3.9+) ===")
    defaults = {"timeout": 30, "retries": 3}
    overrides = {"timeout": 60}
    config = {**defaults, **overrides}
    print(config)
