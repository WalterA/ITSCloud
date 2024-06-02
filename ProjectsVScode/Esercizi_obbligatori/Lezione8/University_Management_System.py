from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self,name:str, age:int):
        super().__init__()
        
        self.name:str = name
        self.age:int = age
    @abstractmethod
    def get_role(self):
        pass
    def __str__(self) -> str:
        return f"Il nome è:{self.name}, la sua età:{self.age}"
class Student(Person):
    def __init__(self,student_id:str,course:list):
        self.student_id = student_id
        self.course = []
        
    def enroll(self):
class Course: