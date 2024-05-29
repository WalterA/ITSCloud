class Person:
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age

        
class Student(Person):
    
    def __init__(self, id: str, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.id: str = id
        self.group = None
        self.interests: list[str] = []
        
    def withdraw(self) -> bool:
        if self.group:
            if self.group.remove_student(self):
                self.group = None
                return True
        return False
    
    def add_interest(self, interest: str):
        self.interests.append(interest)
        
    def get_interests(self) -> list[str]:
        return self.interests
    
    def __str__(self) -> str:
        return f'Student(id={self.id}, cf={self.cf}, name={self.name}'\
            f', surname={self.surname}, age={self.age})'
            
            
class Professor(Person):
    
    def __init__(self, id: str, degree: str,  cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.id: str = id
        self.degree: str = degree
        
    def __str__(self) -> str:
        return f'Prof(id={self.id}, cf={self.cf}, name={self.name}'\
            f', surname={self.surname}, age={self.age}, degree={self.degree})'
            
            
            
studente_1: Student = Student(id=12, cf="dsjfsjn", name="Flavio", surname="Giorgi", age=29)
print(studente_1.name)
print(studente_1.calcola_età())