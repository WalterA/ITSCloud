from film import Film
class Azione(Film):
    def __init__(self, id, title ) -> None:
        super().__init__(id, title)
        self.__azione = "Azione"
        self.__penale = 3.0
    def getGenere(self):
        return self.__azione
    def getPenale(self):
        return self.__penale
    def calcolaPenaleRitardo(self,giorni:float):
        ritardo = giorni * self.getPenale()
        return ritardo
        
class Commedia(Film):
    def __init__(self, id, title) -> None:
        super().__init__(id, title)
        self.__commedia = "Commedia"
        self.__penale = 2.50
    def getGenere(self):
        return self.__commedia
    def getPenale(self):
        return self.__penale
    def calcolaPenaleRitardo(self,giorni:float):
        ritardo = giorni * self.getPenale()
        return ritardo
class Drama(Film):
    def __init__(self, id, title) -> None:
        super().__init__(id, title)
        self.__drama = "Drammatico"
        self.__penale = 2.00
    def getGenere(self):
        return self.__drama
    def getPenale(self):
        return self.__penale
    def calcolaPenaleRitardo(self,giorni:float):
        ritardo = giorni * self.getPenale()
        return ritardo

hotel = Film(123,"gigi")
genere=Drama(123,"gigi" )
print(genere.getGenere())
print(genere.getID())
print(genere.calcolaPenaleRitardo(5))
