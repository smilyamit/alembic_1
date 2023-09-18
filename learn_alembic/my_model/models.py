from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    name: str
    age: str
    score: int
    id: Optional[int] = None

@dataclass
class Course:
    course_name: str
    id: Optional[int] = None
