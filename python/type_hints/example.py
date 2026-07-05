"""Type hints examples — static typing in Python."""

from dataclasses import dataclass
from typing import Callable, Generic, Optional, TypeVar, Union


def greet(name: str, times: int = 1) -> str:
    return (f"Hello, {name}! " * times).strip()


def process_items(items: list[int]) -> dict[str, int]:
    return {"count": len(items), "sum": sum(items)}


@dataclass
class User:
    id: int
    name: str
    email: Optional[str] = None


T = TypeVar("T")


class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def map(self, fn: Callable[[T], T]) -> "Box[T]":
        return Box(fn(self.value))


def parse_id(value: Union[int, str]) -> int:
    if isinstance(value, int):
        return value
    return int(value)


if __name__ == "__main__":
    print(greet("Alice", 2))
    print(process_items([1, 2, 3, 4]))

    user = User(id=1, name="Bob")
    print(user)

    box = Box(10)
    print(box.map(lambda x: x * 2).value)

    print(parse_id("42"))
