from film import Film
from movie_genre import Azione , Drama, Commedia
class Noleggio:
    def __init__(self,film_list:list) -> None:
        self.lista = film_list
        self.rented_film:dict = {}
    def isAvaible(self,film:Film):
        """tale metodo deve ritornare True se il film passato come argomento è 
        presente nell'inventario del negozio, false in caso contrario. Se il film
        è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!".
        Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!"."""
        if film in self.lista:
            print(f"Il film scelto è disponibile: {film}!")
            return True
        else:
            print(f"Il film scelto è disponibile: {film}!")
            return False
    def rentAMovie(self,film:Film, clientID):
        """rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film 
        ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. 
        Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto,
        il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, 
        rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
        la chiave sarà l'id del cliente che noleggia (id_client)
        il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente."""
        if self.isAvaible(film):
            self.lista.remove(film)
            if clientID in self.rented_film:
                self.rented_film[clientID].append(film)
            else:
                self.rented_film[clientID]= [film]
            print (f"Il cliente {clientID} ha noleggiato {film}!")
        else:
            print(f"Non è possibile nolegiare il film {film}!")
    def giveBack(self,film, clientID, days):
        if clientID in self.rented_film:
            self.rented_film[clientID].pop(film)
            self.lista.append(film)
            

    """giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio,
    ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero 
    dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla 
    lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei 
    film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente
    deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}!
    La penale da pagare per il film {titolo_film} e' di {tot} euro!"."""