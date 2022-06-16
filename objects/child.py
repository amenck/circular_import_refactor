from dataclasses import dataclass

from objects import Person


@dataclass(frozen=True)
class Child(Person):
    grade: str

