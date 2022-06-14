from dataclasses import dataclass

from person import Person


@dataclass(frozen=True)
class Child(Person):
    grade: str

