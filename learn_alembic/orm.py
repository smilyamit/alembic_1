from sqlalchemy import Table, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry
from my_model import models
from my_model.models import Base


mapper_reg = registry()
# Base = declarative_base()

student_info = Table(
    'stud',
    mapper_reg.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('name', String),
    Column('age', String)
)

course_info = Table(
    'course_info',
    mapper_reg.metadata,
    Column('id', Integer, primary_key=True, index=True),
    Column('course_name', String)
)

def start_mapping():
    mapper_reg.map_imperatively(models.Student, student_info)
    mapper_reg.map_imperatively(models.Course, course_info)
