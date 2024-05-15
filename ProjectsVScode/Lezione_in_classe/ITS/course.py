from building import Building
from group import Group
from person import Student

class Course:
    
    def __init__(self, name: str, building: Building):
        self.name: str = name
        self.building: Building = building
        self.groups: dict[str, Group] = {}
        
    def register(self, student: Student, preferred_group: str = None):
        if preferred_group:
            group: Group = self.groups.get(preferred_group, None)
            if group:
                add = group.add_student(student)
                if not add:
                    self.__register(student)
        else:
            self.__register(student)

    def __register(self, student):
        for group in self.groups.values():
            add = group.add_student(student)
            if add:
                break
        
    def get_name(self) -> str:
        return self.name
    
    def get_building(self) -> Building:
        return self.building
    
    def __str__(self) -> str:
        s: str =  f'Course(name={self.name}) which is held in:\n' + self.building.__str__() + "\n"
        s += "With Groups:\n"
        for group in self.groups.values():
            s += group.__str__() + "\n" + "#" * 50 + "\n"
        return s[:-1]