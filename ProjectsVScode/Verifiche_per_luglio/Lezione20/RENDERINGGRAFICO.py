
from abc import ABC, ABCMeta, abstractmethod

class Forma(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def getArea(self):
        pass

    @abstractmethod
    def render(self):
        pass

class Quadrato(Forma):
    def __init__(self, lato):
        super().__init__("Quadrato")
        self.lato = lato

    def getArea(self):
        return self.lato * self.lato

    def render(self):
        for i in range(self.lato):
            for j in range(self.lato):
                if i == 0 or i == self.lato - 1 or j == 0 or j == self.lato - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()  
            
class Rettangolo(Forma):
    def __init__(self, base:float, altezza:float):
        super().__init__("Rettangolo")
        self.base = base
        self.altezza = altezza
        
    def getArea(self):
        return self.base * self.altezza
        
    def render(self):
        for i in range(self.altezza):
            for j in range(self.base):
                if i == 0 or i == self.altezza -1 or j ==  0 or j == self.base -1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    
class Triangolo(Forma):
    def __init__(self, l:float):
        super().__init__("Triangolo")
        self.l = l
    def getArea(self):
        return float((self.l *self.l) //2)
        
    def render(self):
        for i in range(1, self.l + 1):
            for j in range(1, i + 1):
                if i == self.l or j == 1 or j == i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print() 
       
tringolo=Triangolo(4)
print(tringolo.getArea())
tringolo.render()
# Esempio di utilizzo:
# quadrato = Quadrato(4)
# print("Nome della forma:", quadrato.nome)
# print("Area del quadrato:", quadrato.getArea())
# quadrato.render()

# rettangolo = Rettangolo(8,4)
# print(rettangolo.getArea())
# rettangolo.render()
