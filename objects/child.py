from dataclasses import dataclass

from objects.person import Person


@dataclass(frozen=True)
class Child(Person):
    grade: str

