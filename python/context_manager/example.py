"""Context manager examples — the `with` statement."""

from contextlib import contextmanager


# --- Class-based context manager ---
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # Return False to propagate exceptions; True to suppress them
        return False


# --- Generator-based with @contextmanager ---
@contextmanager
def temp_value(obj, attr, new_value):
    """Temporarily set an attribute, then restore it."""
    old_value = getattr(obj, attr)
    setattr(obj, attr, new_value)
    try:
        yield obj
    finally:
        setattr(obj, attr, old_value)


class Config:
    debug = False


if __name__ == "__main__":
    print("=== @contextmanager ===")
    cfg = Config()
    print(f"Before: debug={cfg.debug}")
    with temp_value(cfg, "debug", True):
        print(f"Inside:  debug={cfg.debug}")
    print(f"After:  debug={cfg.debug}")

    print("\n=== Class-based (conceptual) ===")
    print("FileManager opens a file in __enter__ and closes in __exit__")
