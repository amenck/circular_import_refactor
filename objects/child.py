from dataclasses import dataclass

from objects.parent import Person


@dataclass(frozen=True)
class Child(Person):
    grade: str

