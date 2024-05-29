from abc import ABC, abstractmethod

class abcAnimal(ABC):
    @abstractmethod
    def verso(self):
        pass
    
    
    

class Cane(abcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome: str = nome
    
    def verso(self):
        print("Bau!")
        
        
class Gatto(abcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome: str = nome
    
    def verso(self):
        print("Miao!")
        
class Coccodrillo(abcAnimal):
    def __init__(self,nome:str) -> None:
        self.nome: str = nome
        
    
    def verso(self):
        print("Miao!")

from typing import Any
from typing import TypeAlias    
tipoComposto: TypeAlias = dict[int,int]

a:dict[str,str | int] = {"key":"val_1","key_3":3} # OR LOGICO |        
cane_1:Cane = Cane(nome="PLUTO")
gatto_1:Gatto = Gatto(nome="Silvestro")
Coccodrillo_1 :Coccodrillo = Coccodrillo(nome="Giovanni")


lista_animali:list[abcAnimal] = [cane_1,gatto_1,Coccodrillo_1]

for animali in lista_animali:
    animali.verso()


gatto_1.verso()
Coccodrillo_1.verso()
cane_1.verso()