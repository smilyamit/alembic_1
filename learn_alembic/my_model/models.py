from dataclasses import dataclass
from typing import Optional

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


@dataclass
class Student:
    name: str
    age: str
    id: Optional[int] = None

@dataclass
class Course:
    course_name: str
    id: Optional[int] = None
