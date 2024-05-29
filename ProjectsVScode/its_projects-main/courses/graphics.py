
from courses.course_abstract import CourseAB
from person import Student


class ComputerGraphicsCourse(CourseAB):
    
    def __init__(self, name: str, prerequisite: str = "Graphics"):
        super().__init__(name)
        self.prerequisite: str = prerequisite
        
    def register_student(self, student: Student):
        if self.prerequisite in student.get_interests():
            for group in self.groups:
                if group.add_student(student):
                    break