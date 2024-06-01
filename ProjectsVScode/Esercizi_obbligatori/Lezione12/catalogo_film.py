class MovieCatalog:
    def __init__(self) -> None:
        self.catalog:dict = {}

    def add_movie(self, director_name, movies):

        if director_name in self.catalog and set(movies).issubset(set(self.catalog[director_name])):
            print(f"I film {movies} del regista {director_name} sono già presenti nel catalogo.")
        else:
            # Aggiunta dei film al catalogo
            if director_name in self.catalog:
                self.catalog[director_name].extend(movies)
            else:
                self.catalog[director_name] = movies
    def __str__(self) -> str:
        return str(self.catalog)

    def remove_movie(self, director_name, movie_name):
        if director_name in self.catalog and movie_name in self.catalog[director_name]:
            self.catalog[director_name].remove(movie_name)
            if not self.catalog[director_name]:
                del self.catalog[director_name]

    def list_directors(self):
        for director in self.catalog.items():
            print(f"I registri sono: {director[0]}")
            
    def get_movie_by_director(self, director_name):
        if director_name in self.catalog:
            movies = self.catalog[director_name]
            print(f"Film del regista: {director_name}, titolo: {movies}")
        else:
            print(f"Regista {director_name} non trovato nel catalogo.")

    def search_movie_by_title(self, title):
        found_movies = {}
        for director, movies in self.catalog.items():
            for movie in movies:
                if title in movie:
                    if director in found_movies:
                        found_movies[director].append(movie)
                    else:
                        found_movies[director] = [movie]
        if found_movies:
            return found_movies
        else:
            return "Nessun film trovato con la parola nel titolo."

                
                    
                    
        

"""------------------------PRINT------------------------------"""
armenice = MovieCatalog()
armenice.add_movie("sono io", ["3 metri non di cielo","bomba"])
armenice.add_movie("sono io", ["3 metri non di cielo"])
armenice.add_movie("figoguuu", ["pasta al pesto"])
armenice.add_movie("titi", ["fumo poco", "daglie", "ore "])
print(armenice)
armenice.remove_movie("sono io","3 metri non di cielo")
print(armenice)
armenice.list_directors()
armenice.get_movie_by_director("sono io")
print(armenice.search_movie_by_title("d"))