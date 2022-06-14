from dataclasses import dataclass
from typing import List

from child import Child


@dataclass(frozen=True)
class Person:
    name: str
    age: int


@dataclass(frozen=True)
class Parent(Person):
    children: List[Child]

