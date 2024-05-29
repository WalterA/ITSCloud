
from config import PYTHON_CLASSES
from materials.material_abstract import AbstractLesson
from person import Student


class ClassesInPythonLesson(AbstractLesson):
    
    def __init__(self, previous_lesson: AbstractLesson):
        super().__init__(name=PYTHON_CLASSES['NAME'],
                         subjects=PYTHON_CLASSES['SUBJECTS'],
                         duration=PYTHON_CLASSES['DURATION'],
                         difficulty=PYTHON_CLASSES['DIFFICULTY'])
        
        self.previous_lesson: AbstractLesson = previous_lesson
        
    def grade_student(self, student: Student) -> float:
        return 10