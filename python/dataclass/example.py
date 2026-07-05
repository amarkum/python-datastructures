"""Dataclass — boilerplate-free data containers."""

from dataclasses import dataclass, field, asdict, replace
from typing import ClassVar


@dataclass
class Point:
    x: float
    y: float

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass(frozen=True, order=True)
class ImmutableUser:
    id: int
    name: str


@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)
    MAX_SIZE: ClassVar[int] = 10

    def add_member(self, member):
        self.members.append(member)


if __name__ == "__main__":
    print("=== Basic dataclass ===")
    p = Point(3.0, 4.0)
    print(p, p.distance_from_origin())

    print("\n=== frozen + order ===")
    u1 = ImmutableUser(1, "Alice")
    u2 = ImmutableUser(2, "Bob")
    print(u1 < u2)

    print("\n=== default_factory (mutable default trap avoided) ===")
    t1 = Team("Alpha")
    t2 = Team("Beta")
    t1.add_member("Amar")
    print(t1.members, t2.members)

    print("\n=== asdict / replace ===")
    print(asdict(p))
    print(replace(p, x=10.0))
