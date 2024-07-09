from abc import ABC, abstractmethod



class Animal(ABC):
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__()
        
        self.name: str = name
        self.age: int = age
        
    @abstractmethod
    def verso(self):
        pass
    
    
class Cat(Animal):
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        
    def verso(self):
        print("Miao!")
        
        
class Dog(Animal):
    
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        
    def verso(self):
        print("Bau!")
        
        
class Horse(Animal):
    
    
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        
    def verso(self):
        print("Hyhyhyhyh!")
        
    
    
lista_animali: list[Animal] = [Dog("Fido", 12), Cat("Silvestro", 10), Horse("Spirit", 15)]    
for animale in lista_animali:
    
    animale.verso()

cane_1: Dog = Dog(name="Fido", age=3)

cavallo_1: Horse = Horse(name="Spirit", age=10)

cane_1.verso()
cavallo_1.verso()
