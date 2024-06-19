from materials.material_abstract import AbstractLesson
from person import Professor, Student

class Group:
    
    def __init__(self, name: str, limit_students: int):
        self.name: str = name
        self.limit_students: int = limit_students
        self.students: list[Student] = []
        self.professors: list[Professor] = []
        self.materials: list[AbstractLesson] = []
    
    def add_student(self, student: Student) -> bool:
        if student not in self.students and self.get_limit_students() > 0:
            self.students.append(student)
            self.limit_students -= 1
            student.group = self
            return True
        return False
    
    def remove_student(self, student: Student) -> bool:
        if student in self.students:
            self.students.remove(student)
            self.limit_students += 1
            return True
        return False
    
    def add_professor(self, professor: Professor) -> bool:
        if professor not in self.professors and self.get_limit_professors() > len(self.professors):
            self.professors.append(professor)
            return True
        return False
    
    def add_material(self, lesson: AbstractLesson):
        self.materials.append(lesson)
            
    def get_limit_professors(self) -> int:
        return max(len(self.students) // 10, 1)
        
    def get_name(self) -> str:
        return self.name
    
    def get_limit_students(self) -> int:
        return self.limit_students
    
    def __str__(self) -> str:
        s: str = f'Group(name={self.get_name()}, limit_students={self.get_limit_students()})'
        s += "\nWith Student:\n"
        for student in self.students:
            s += student.__str__() + "\n"
        s += "With Professors:\n"
        for prof in self.professors:
            s += prof.__str__() + "\n"
        s += "With Lessons:\n"
        for lesson in self.materials:
            s += lesson.__str__() + "\n"
        return s[:-1]