from movie_genre import Azione, Commedia, Drama

class Noleggio:
    def __init__(self, film_list):
        self.film_list = film_list
        self.rented_film = {}
    
    def isAvaible(self, film):
        if film in self.film_list:
            print(f"Il film scelto è disponibile: {film.getTitle()}!")
            return True
        else:
            print(f"Il film scelto non è disponibile: {film.getTitle()}!")
            return False
    
    def rentAMovie(self, film, clientID):
        if self.isAvaible(film):
            self.film_list.remove(film)
            if clientID not in self.rented_film:
                self.rented_film[clientID] = []
            self.rented_film[clientID].append(film)
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")
    
    def giveBack(self, film, clientID, days):
        if clientID in self.rented_film and film in self.rented_film[clientID]:
            self.rented_film[clientID].remove(film)
            if not self.rented_film[clientID]:
                del self.rented_film[clientID]
            self.film_list.append(film)
            penale = film.calcolaPenaleRitardo(days)
            print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")
        else:
            print(f"Il film {film.getTitle()} non è stato noleggiato dal cliente {clientID}!")
    
    def printMovies(self):
        for film in self.film_list:
            print(f"{film.getTitle()} - {film.getGenere()} -")
    
    def printRentMovies(self, clientID):
        if clientID in self.rented_film:
            for film in self.rented_film[clientID]:
                print(f"{film.getTitle()} - {film.getGenere()} -")
        else:
            print(f"Nessun film noleggiato dal cliente {clientID}.")



# Creare alcune istanze di film
film1 = Azione(1, "Mad Max: Fury Road")
film2 = Commedia(2, "Superbad")
film3 = Drama(3, "The Shawshank Redemption")
film4 = Azione(4, "Die Hard")
film5 = Drama(5, "The Godfather")

# Creare una lista di film disponibili in negozio
film_list = [film1, film2, film3, film4, film5]

# Creare un'istanza di Noleggio con la lista dei film
noleggio = Noleggio(film_list)

# Stampare i film disponibili in negozio
print("Film disponibili in negozio:")
noleggio.printMovies()

# Esempio di noleggio di un film
client_id = 101
noleggio.rentAMovie(film1, client_id)
noleggio.rentAMovie(film3, client_id)

# Stampare i film noleggiati dal cliente
print(f"\nFilm noleggiati dal cliente {client_id}:")
noleggio.printRentMovies(client_id)

# Stampare i film disponibili dopo il noleggio
print("\nFilm disponibili in negozio dopo il noleggio:")
noleggio.printMovies()

# Restituire un film
days_late = 5
noleggio.giveBack(film1, client_id, days_late)

# Stampare i film disponibili dopo la restituzione
print("\nFilm disponibili in negozio dopo la restituzione:")
noleggio.printMovies()

# Stampare i film noleggiati dal cliente dopo la restituzione
print(f"\nFilm noleggiati dal cliente {client_id} dopo la restituzione:")
noleggio.printRentMovies(client_id)


# from film import Film
# from movie_genre import Azione , Drama, Commedia
# from abc import abstractmethod

# class Noleggio:
#     def __init__(self,film_list:list) -> None:
#         self.lista = film_list
#         self.rented_film:dict = {}
#     def isAvaible(self,film:Film):
#         """tale metodo deve ritornare True se il film passato come argomento è 
#         presente nell'inventario del negozio, false in caso contrario. Se il film
#         è disponibile in negozio stampare: "Il film scelto è disponibile: {titolo_film}!".
#         Se il film non è disponibile in negozio stamapre: "Il film scelto è disponibile: {titolo_film}!"."""
#         if film in self.lista:
#             print(f"Il film scelto è disponibile: {film.getTitle()}!")
#             return True
#         else:
#             print(f"Il film scelto è disponibile: {film.getTitle()}!")
#             return False
#     def rentAMovie(self,film:Film, clientID):
#         """rentAMovie(film, clientID): tale metodo deve gestire il noleggio di un film 
#         ed ha come argomenti il film da noleggiare ed il codice id del cliente che lo noleggia. 
#         Affinché sia possibile noleggiare un film, un film deve essere disponibile in negozio. Pertanto,
#         il metodo deve verificare la disponibilità. Nel caso in cui il film richiesto sia disponibile, 
#         rimuoverlo dalla lista dei film disponibili in negozio, poi riempire il dizionario rented_film in questo modo:
#         la chiave sarà l'id del cliente che noleggia (id_client)
#         il corrispondente valore sarà una lista contenente i film noleggiati da quel cliente."""
        
#         if self.isAvaible(film):    
#             self.lista.remove(film)
#             if clientID in self.rented_film:
#                 self.rented_film[clientID].append(film)
#             else:
#                 self.rented_film[clientID]=[film]
#             print (f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
            
            
#     def giveBack(self,film:Film, clientID, days):
#         if clientID in self.rented_film and film in self.rented_film[clientID]:
#             self.rented_film[clientID].remove(film)
#             if not self.rented_film[clientID]:
#                 del self.rented_film[clientID]
#             self.film_list.append(film)
#             penale = film.calcolaPenaleRitardo(days)
#             print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")
#         else:
#             print(f"Il film {film.getTitle()} non è stato noleggiato dal cliente {clientID}!")
#     """giveBack(film, clientID, days): questo metodo consente di restituire un film noleggiato in negozio,
#     ed ha come argomenti il film da restituire, il codice ID del client che restituisce il film, il numero 
#     dei giorni in cui il cliente ha tenuto il film per se.  Il film da restituire deve essere rimosso dalla 
#     lista dei film noleggiati dal cliente con id clientID, e tale film, deve essere riaggiunto alla lista dei 
#     film disponibili in negozio (film_list). Successivamente, il metodo deve calcolare la penale che il cliente
#     deve pagare utilizzando l'opposito metodo. Stampare la penale che il cliente deve pagare: "Cliente: {clientID}!
#     La penale da pagare per il film {titolo_film} e' di {tot} euro!"."""
# #--------------------------------print--------------------------
# hotel = Film(1235,"gigi")
# hotel.setID(456)
# hotel.setTitle("fe")
# genere=Drama(123,"drami" )
# a = Film(123,"gigi")
# a.setID(4567)
# a.setTitle("fefe")
# b = Film(123,"gigi")
# b.setID(4568)
# b.setTitle("fefefefe")
# genere=Commedia(123,"ed" )
# c = Film(123,"gigi")
# c.setID(4569)
# c.setTitle("fefegnr")
# genere=Azione(123,"ok" )

# lista=[]
# bl = Noleggio(lista)
# bl.isAvaible(hotel)
# bl.isAvaible(a)
# bl.isAvaible(b)
# bl.isAvaible(c)
# bl.rentAMovie(hotel, 123)
# bl.rentAMovie(hotel,123)
# bl.rentAMovie(a,123)
# bl.rentAMovie(a,123)
# bl.rentAMovie(b,455)
# print(bl.giveBack(a,123,10))
