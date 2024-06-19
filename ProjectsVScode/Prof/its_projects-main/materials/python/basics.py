

from config import PYTHON_BASICS
from materials.material_abstract import AbstractLesson
from person import Student


class PythonBasics(AbstractLesson):
    
    def __init__(self):
        super().__init__(name=PYTHON_BASICS['NAME'],
                         subjects=PYTHON_BASICS['SUBJECTS'],
                         duration=PYTHON_BASICS['DURATION'],
                         difficulty=PYTHON_BASICS['DIFFICULTY'])
    
    def grade_student(self, student: Student) -> float:
        if student.age > 30:
            return 8
        elif 18 < student.age < 30:
            return 9
        else:
            return 6