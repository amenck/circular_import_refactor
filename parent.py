from dataclasses import dataclass
from typing import List

from person import Person
from child import Child


@dataclass(frozen=True)
class Parent(Person):
    children: List[Child]

