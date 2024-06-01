import unittest
import sys
import os

# Aggiungi il percorso principale del progetto al sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ProjectsVScode.Esercizi_obbligatori.lepre_tartaruga.lepre_tartaruga import loop, mossa_lepre, mossa_tartaruga, dado

class TestLepreTartaruga(unittest.TestCase):

    def test_dado(self):
        for _ in range(100):
            roll = dado()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 10)

    def test_mossa_tartaruga(self):
        movimento, energia = mossa_tartaruga(100, 'sole')
        self.assertIn(movimento, [-6, 1, 3])
        self.assertGreaterEqual(energia, 0)

        movimento, energia = mossa_tartaruga(0, 'sole')
        self.assertEqual(energia, 10)

    def test_mossa_lepre(self):
        movimento, energia = mossa_lepre(100, 'sole')
        self.assertIn(movimento, [0, 1, 9, -2, -12])
        self.assertGreaterEqual(energia, 0)

        movimento, energia = mossa_lepre(0, 'sole')
        self.assertEqual(energia, 10)

    def test_loop(self):
        # Esegui il loop una volta per assicurarti che funzioni senza errori.
        # Non verifichiamo l'output qui, solo che non ci siano errori di esecuzione.
        loop()

if __name__ == "__main__":
    unittest.main()
