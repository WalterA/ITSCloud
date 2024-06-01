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

    def __init__(self):
        self.magazzino:list[Prodotto] = []

    def aggiungi_prodotto(self, prodotto: Prodotto):
        self.magazzino.append(prodotto)


    def cerca_prodotto(self,nome: str):
        for prodotto in self.magazzino:
            if prodotto.nome == nome:
                return prodotto

    def verifica_disponibilità(self,nome: str)->str:
        prodotto = self.cerca_prodotto(nome)
        if prodotto is not None:
            return f"Il prodotto '{nome}' è disponibile."
        else:
            return f"Il prodotto '{nome}' non è disponibile."
"""-------------------------------------------PRINT---------------------------------"""
gomme = Prodotto("bmv", 5)
ruota = Prodotto("tigre", 3)
auto = Prodotto("jagur", 2)
print(auto)
ugo_spa= Magazzino()
ugo_spa.aggiungi_prodotto(gomme)
ugo_spa.aggiungi_prodotto(ruota)
ugo_spa.aggiungi_prodotto(auto)
print(ugo_spa.verifica_disponibilità("bm"))
