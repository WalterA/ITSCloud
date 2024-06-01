"""Classi:
- Film: Rappresenta un film con titolo e durata.
 
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
 
- Cinema: Gestisce le operazioni legate alla gestione delle sale.

Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

Test case:

    Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
    Un cliente sceglie un film e prenota un certo numero di posti.
    Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

"""
class Film:

    def __init__(self,titolo:str,durata:float) -> None:
        self.titolo:str = titolo
        self.durata:float = durata

class Sala:

    def __init__(self,id:int,film:Film,posti_tot:int) -> None:
        self.id:int = id
        self.film:Film = film
        self.posti_tot:int = posti_tot
        self.posti_prenotati:int = 0

    def prenota_posti(self,posti_prenotati:int) -> str:
        """Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore."""
        if self.posti_tot > posti_prenotati:
            self.posti_tot -= posti_prenotati
            return f"Posti prenotati sono:{posti_prenotati}"
        else:
            return "Non ci sono posti disponibili"

    def posti_disponibili(self)->str:
        """Restituisce il numero di posti ancora disponibili nella sala."""
        return f"Posti disponibili sono:{self.posti_tot}"

class Cinema:

    """- aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti.
    Restituisce un messaggio di stato.
    """

    def __init__(self) -> None:
        self.tutte_sale:list[Sala] = []


    def aggiungi_sala (self,sala: Sala)->None:
        self.tutte_sale.append(sala)
        return

    def prenota_film(self, titolo_film: str, num_posti: int) -> str:
        for elem in self.tutte_sale:
            if elem.film.titolo == titolo_film:
                elem.prenota_posti(num_posti)
                return "Posti prenotati"
        return f"Film {titolo_film} non trovato"

"""_____________________Print________________________________"""
film:Film = Film("Corte",3.40)
film2:Film = Film("BOBO",3.43)
sala:Sala = Sala(12353253,film,40)
sala2 = Sala(23232,film2, 30)
print(sala.prenota_posti(5))
print(sala.posti_disponibili())
meraviglia=Cinema()
meraviglia.aggiungi_sala(sala)
meraviglia.aggiungi_sala(sala2)

print(meraviglia.prenota_film("gigi", 5))
print(meraviglia.prenota_film("BOBO", 5))
print(meraviglia.prenota_film("gigi", 5))
print(meraviglia.prenota_film("gigi", 5))
print(meraviglia.prenota_film("Corte", 5))
print(meraviglia.prenota_film("gigi", 5))