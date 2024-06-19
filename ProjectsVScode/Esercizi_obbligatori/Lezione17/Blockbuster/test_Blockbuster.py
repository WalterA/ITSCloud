import unittest
from film import Film
from movie_genre import Azione, Commedia, Drama
from noleggio import Noleggio


class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film1 = Film(1, "Film1")
        self.film2 = Film(2, "Film2")
    
    def test_setID(self):
        self.film1.setID(10)
        self.assertTrue(self.film1.getID(), int)
    
    def test_setTitle(self):
        self.film1.setTitle("NewTitle")
        self.assertTrue(self.film1.getTitle(), str)
    
    def test_getID(self):
        self.assertTrue(self.film1.getID(), int)
    
    def test_getTitle(self):
        self.assertTrue(self.film1.getTitle(), str)
    
    def test_isEqual(self):
        film3 = Film(1, "AnotherFilm")
        self.assertTrue(self.film1.isEqual(film3))
        self.assertFalse(self.film1.isEqual(self.film2))


class TestAzione(unittest.TestCase):
    def setUp(self):
        self.azione = Azione(1, 4)
    
    def test_getGenere(self):
        self.assertTrue(self.azione.getGenere(), str)
    
    def test_getPenale(self):
        self.assertEqual(self.azione.getPenale(), 3.0)
    
    def test_calcolaPenaleRitardo(self):
        self.assertEqual(self.azione.calcolaPenaleRitardo(5), 15.0)

class TestCommedia(unittest.TestCase):
    def setUp(self):
        self.commedia = Commedia(2, "Superbad")
    
    def test_getGenere(self):
        self.assertEqual(self.commedia.getGenere(), "Commedia")
    
    def test_getPenale(self):
        self.assertEqual(self.commedia.getPenale(), 2.5)
    
    def test_calcolaPenaleRitardo(self):
        self.assertEqual(self.commedia.calcolaPenaleRitardo(4), 10.0)

class TestDrama(unittest.TestCase):
    def setUp(self):
        self.drama = Drama(3, "The Shawshank Redemption")
    
    def test_getGenere(self):
        self.assertEqual(self.drama.getGenere(), "Drama")
    
    def test_getPenale(self):
        self.assertEqual(self.drama.getPenale(), 2.0)
    
    def test_calcolaPenaleRitardo(self):
        self.assertEqual(self.drama.calcolaPenaleRitardo(3), 6.0)

class TestNoleggio(unittest.TestCase):

    def setUp(self):
        # Creare alcune istanze di film
        self.film1 = Azione(1, "Mad Max: Fury Road")
        self.film2 = Commedia(2, "Superbad")
        self.film3 = Drama(3, "The Shawshank Redemption")
        self.film4 = Azione(4, "Die Hard")
        self.film5 = Drama(5, "The Godfather")
        
        # Creare una lista di film disponibili in negozio
        self.film_list = [self.film1, self.film2, self.film3, self.film4, self.film5]
        
        # Creare un'istanza di Noleggio con la lista dei film
        self.noleggio = Noleggio(self.film_list)

    def test_isAvaible(self):
        # Test disponibilità di un film
        self.assertTrue(self.noleggio.isAvaible(self.film1))
        self.assertTrue(self.noleggio.isAvaible(self.film5))
        
        # Noleggia un film e verifica che non sia più disponibile
        self.noleggio.rentAMovie(self.film1, 101)
        self.assertFalse(self.noleggio.isAvaible(self.film1))

    def test_rentAMovie(self):
        # Test noleggio di un film disponibile
        client_id = 101
        self.noleggio.rentAMovie(self.film1, client_id)
        self.assertFalse(self.film1 in self.film_list)
        self.assertTrue(self.film1 in self.noleggio.rented_film[client_id])
        
        # Test noleggio di un film non disponibile
        self.noleggio.rentAMovie(self.film1, client_id)  # Questo dovrebbe stampare un messaggio di errore

    def test_giveBack(self):
        client_id = 101
        self.noleggio.rentAMovie(self.film1, client_id)
        self.noleggio.giveBack(self.film1, client_id, 5)
        
        # Verifica che il film sia di nuovo disponibile
        self.assertTrue(self.film1 in self.film_list)
        self.assertFalse(client_id in self.noleggio.rented_film or self.film1 in self.noleggio.rented_film.get(client_id, []))
    
    def test_printMovies(self):
        # Testa la stampa dei film disponibili
        expected_output = "Mad Max: Fury Road - Azione -\nSuperbad - Commedia -\nThe Shawshank Redemption - Drama -\nDie Hard - Azione -\nThe Godfather - Drama -\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        self.noleggio.printMovies()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_printRentMovies(self):
        client_id = 101
        self.noleggio.rentAMovie(self.film1, client_id)
        self.noleggio.rentAMovie(self.film2, client_id)
        
        # Testa la stampa dei film noleggiati dal cliente
        expected_output = "Mad Max: Fury Road - Azione -\nSuperbad - Commedia -\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        self.noleggio.printRentMovies(client_id)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)




if __name__ == '__main__':
    unittest.main()
