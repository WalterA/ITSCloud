from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name: str, age:int) -> None:
        super().__init__()
        
        self.name: str = name
        self.age:int = age
        
    @abstractmethod
    def verso(self):
        pass

class Cat(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
    def verso(self):
        print("Miao")
        
class Dog(Animal):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        
    def verso(self):
        print("Bau")
        
        
cane1: Dog = Dog(name="davide", age=3)
cane1.verso()
