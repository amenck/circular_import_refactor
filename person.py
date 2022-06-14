from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class Person:
    name: str
    age: int

