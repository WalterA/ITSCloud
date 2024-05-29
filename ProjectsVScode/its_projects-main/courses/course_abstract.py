from abc import ABC
from abc import abstractmethod

from group import Group
from person import Student

class CourseAB(ABC):
    
    def __init__(self, name: str):
        super().__init__()
        self.name: str = name
        self.groups: list[Group] = []
        
    @abstractmethod
    def register_student(self, student: Student):
        pass
    
    def common_subjects(self, group1: Group, group2: Group) -> set[str]:
        subjects_group1: set[str] = self.__get_group_subjects(group1)
        subjects_group2: set[str] = self.__get_group_subjects(group2)
        return subjects_group1.intersection(subjects_group2)
    
    def difference_subjects(self, group1: Group, group2: Group) -> set[str]:
        subjects_group1: set[str] = self.__get_group_subjects(group1)
        subjects_group2: set[str] = self.__get_group_subjects(group2)
        return subjects_group1.difference(subjects_group2)
    
    def __get_group_subjects(self, group: Group) -> set[str]:
        subjects: list[str] = []
        for material in group.materials:
            subjects += material.subjects
        return set(subjects)
    
    def add_group(self, group: Group):
        self.groups.append(group)
        
    def get_name(self) -> str:
        return self.name
    
    def __str__(self) -> str:
        s: str =  f'Course(name={self.name})\n'
        s += "With Groups:\n"
        for group in self.groups:
            s += group.__str__() + "\n" + "#" * 50 + "\n"
        return s[:-1]
    