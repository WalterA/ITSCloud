from building import Building
from courses.course_abstract import CourseAB
from person import Student


class PythonCourse(CourseAB):
    
    def __init__(self, name: str, building: Building):
        super().__init__(name)
        self.building: Building = building
        
    def register_student(self, student: Student):
        for group in self.groups:
            if group.add_student(student):
                break