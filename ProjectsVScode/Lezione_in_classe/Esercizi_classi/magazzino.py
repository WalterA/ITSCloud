"""Definisci una classe Prodotto con i seguenti attributi:
- nome (stringa)
- quantità (intero)
 
Definisci una classe Magazzino con i seguenti metodi:
- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
 """
 
class Prodotto:
    
    def __init__(self,nome:str,quantita:int) -> None:
        self.nome = nome
        self.quantita = quantita
        
class Magazzino:
    
    def __init__(self) -> None:
        self.magazzino:list[Prodotto] = []
    
    def aggiungi_prodotto(self, prodotto: Prodotto)->None:
        self.magazzino.append(prodotto)
        return
    
    def cerca_prodotto(self,nome: str)-> str:
        for prodotto in self.magazzino:
            if prodotto.nome == nome:
                return nome
            
    def verifica_disponibilità(self,nome: str) -> str:
        if self.cerca_prodotto(nome) == nome:
            return f"Il prodotto: {nome} è disponibile"
        
gomme = Prodotto("bmv", 5)
Magazzino.aggiungi_prodotto(gomme)
Magazzin.cerca_prodotto()
    
        
    