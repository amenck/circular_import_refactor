from dataclasses import dataclass
from typing import List

from parent import Person


@dataclass(frozen=True)
class Child(Person):
    grade: str

