class Filiale:
    
    filiali_create: int = 0
    
    def __init__(self, codice: str, indirizzo: str) -> None:
        
        self.codice = codice
        self.indirizzo = indirizzo
        
        Filiale.filiali_create += 1
        
    @classmethod
    def totale_filiali_create(cls) -> int:
        
        return cls.filiali_create

class Banca:
    
    def __init__(self, nome: str, simbolo: str) -> None:
        
        self.nome: str = nome
        self.simbolo: str = simbolo
        self.lista_filiali: list[Filiale] = []
        
    def numero_filiali(self) -> int:
        
        return len(self.lista_filiali)
       
       
    def aggiungi_filiale(self, filiale: Filiale):
        
        
        if self.simbolo in filiale.codice:
            
            self.lista_filiali.append(filiale)
        else:
            raise ValueError(f"La filiale appartiene ad un'altra banca!")
       




unicredit: Banca = Banca(nome="Unicredit", simbolo="UCG")
intesa: Banca = Banca(nome="Intesa San Paolo", simbolo="ISP")

filiale_unicredit_1: Filiale = Filiale(codice="UCG01", 
                                       indirizzo="Via Sierra Nevada, 60, Roma, Italia")

filiale_intesa_1: Filiale = Filiale(codice="ISP01", 
                                       indirizzo="Piazza Barberini, 60, Roma, Italia")


intesa.aggiungi_filiale(filiale_intesa_1)
unicredit.aggiungi_filiale(filiale_unicredit_1)

print(unicredit.numero_filiali())
print(intesa.numero_filiali())
print(Filiale.totale_filiali_create())