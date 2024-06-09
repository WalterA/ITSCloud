"""
1. Classe Specie

- Attributi:
nome (str): Nome della specie.
popolazione (int): Popolazione iniziale.
tasso_crescita (float): Tasso di crescita annuo percentuale.
- Metodi:
__init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
Costruttore per inizializzare gli attributi della classe.
cresci(self): Metodo per aggiornare la popolazione per l'anno successivo.
anni_per_superare(self, altra_specie: 'Specie') -> int: Metodo per calcolare in quanti anni 
la popolazione di questa specie supererà quella di un'altra specie.
getDensita(self, area_kmq: float) -> int: Metodo per calcolare in quanti anni la popolazione
raggiungerà una densità di 1 individuo per km².
import math
"""
class Specie:
    def __init__(self, nome: str, popolazione_iniziale: int, tasso_crescita: float):
        self.nome = nome
        self.popolazione = popolazione_iniziale
        self.tasso_crescita = tasso_crescita / 100  # Converti il tasso di crescita in decimale

    def cresci(self):
        self.popolazione = int(self.popolazione * (1 + self.tasso_crescita))
    
    def anni_per_superare(self, altra_specie: 'Specie') -> int:
        anni = 0
        pop_self = self.popolazione
        pop_altra = altra_specie.popolazione
        
        while pop_self <= pop_altra:
            pop_self *= (1 + self.tasso_crescita)
            pop_altra *= (1 + altra_specie.tasso_crescita)
            anni += 1
        
        return anni

    def anni_per_densita(self, area_kmq: float) -> int:
        anni = 0
        pop_self = self.popolazione
        
        while pop_self < area_kmq:
            pop_self *= (1 + self.tasso_crescita)
            anni += 1
        
        return anni

# Esempio di utilizzo
bufali_klingon = Specie("Bufali Klingon", 1000, 5)  # 1000 individui, tasso di crescita 5%
elefanti = Specie("Elefanti", 800, 8)  # 800 individui, tasso di crescita 8%

# Calcola in quanti anni la popolazione degli Elefanti supererà quella dei Bufali Klingon
anni_superamento = elefanti.anni_per_superare(bufali_klingon)
print(f"Popolazione degli Elefanti supererà quella dei Bufali Klingon in {anni_superamento} anni.")

# Calcola in quanti anni la popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km²
area_riserva = 2000  # area della riserva in km²
anni_densita = bufali_klingon.anni_per_densita(area_riserva)
print(f"Popolazione dei Bufali Klingon raggiungerà una densità di 1 individuo per km² in {anni_densita} anni.")
