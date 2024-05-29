

from courses.course_abstract import CourseAB
from person import Student


class JavaCourse(CourseAB):
    
    def __init__(self, name: str, max_age: int):
        super().__init__(name)
        self.max_age = max_age
        
    def register_student(self, student: Student):
        if student.age <= self.max_age:
            for group in self.groups: # O(m)
                if group.add_student(student):
                    break