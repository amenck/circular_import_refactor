from dataclasses import dataclass
from typing import List

from objects import Child, Person


@dataclass(frozen=True)
class Parent(Person):
    children: List[Child]

