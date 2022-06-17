from dataclasses import dataclass
from typing import List

from objects import Child
from objects.person import Person


@dataclass(frozen=True)
class Parent(Person):
    children: List[Child]

