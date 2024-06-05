"""Si desidera sviluppare un sistema per la gestione 
di una biblioteca in Python. Il sistema deve permettere 
di gestire un inventario di libri e le operazioni di prestito 
e restituzione degli stessi. Gli utenti del sistema devono essere in 
grado di aggiungere libri al catalogo, prestarli, restituirli e visualizzare 
quali libri sono disponibili in un dato momento.
 
Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito.
Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una
biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al
    catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, 
    se disponibile e non già prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e,
    se trovato e prestato, lo segna come disponibile. Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli 
    dei libri attualmente disponibili. Se non ci sono libri disponibili, 
    restituisce un messaggio di errore."""

class Libro:

    def __init__(self,titolo:str,autore:str) -> None:
        self.titolo = titolo
        self.autore = autore
        self.prestito = False

class Biblioteca:
    def __init__(self) -> None:
        self.catalogo:list[Libro] = []

    def aggiungi_libro(self,libro:Libro):
        for elem in self.catalogo:
            if elem == libro:
              return f"il libro: {libro.titolo} è già presente"
        self.catalogo.append(libro)
        return f"Libro aggiunto nel catalogo, il libro è: {libro.titolo}"

    def presta_libro(self,titolo):
        for elem in self.catalogo:
            if elem.titolo == titolo and not elem.prestito:
                elem.prestito = True
                return f"libro:{titolo} è stato prestato"
        return f"libro:{titolo} non è disponibile"

    def restituisci_libro(self,titolo):
        for elem in self.catalogo:
            if elem.titolo == titolo and elem.prestito:
                elem.prestito = False
                return f"libro:{titolo} è stato restituito"
        return f"libro:{titolo} è già disponibile"

    def mostra_libri_disponibili(self):
        disponibili = []
        for elem in self.catalogo:
            if not elem.prestito:
                disponibili.append(elem.titolo)
            elif len(disponibili) == 0:
                return f"Libri non disponibili"
        return  disponibili




"""-----------------------PRINT-----------------------"""
gigi= Libro("ugo nel bosco", "gigi d'agostino")
fabio= Libro("ugo in casa", "franco di ieri")
andre= Libro("ugo che caga", "domenico di domenica")
francp= Libro("ugo va in mot", "umberto primo quello vero")
jho= Libro("ugo la vita ", "francesco de agostini")
Feltrinellina = Biblioteca()
print(Feltrinellina.aggiungi_libro(gigi))
print(Feltrinellina.aggiungi_libro(fabio))
print(Feltrinellina.aggiungi_libro(andre))
print(Feltrinellina.aggiungi_libro(francp))
print(Feltrinellina.aggiungi_libro(jho))
print(Feltrinellina.presta_libro("ugo nel bosco"))
print(Feltrinellina.presta_libro("ugo in casa"))
print(Feltrinellina.presta_libro("ugo che caga"))
print(Feltrinellina.presta_libro("ugo va in mot"))
print(Feltrinellina.presta_libro("ugo la vita "))
# print(Feltrinellina.restituisci_libro("ugo nel bosco"))
# print(Feltrinellina.restituisci_libro("ugo nel bosco"))
print(Feltrinellina.mostra_libri_disponibili())

