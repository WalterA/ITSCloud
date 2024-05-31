import unittest
from src.bardh_zoo import Zoo,ZooKeeper,Animal,Fence

class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")
    
    def test_initial_health(self):
        self.assertEqual(self.simba.health, 20.0)  # Health is calculated as min(round(100 * (1/age), 3), 100)

    def test_area(self):
        self.assertEqual(self.simba.area(), 6)

    def test_become_bigger(self):
        new_height, new_width = self.simba.become_bigger()
        self.assertAlmostEqual(new_height, 2.04)
        self.assertAlmostEqual(new_width, 3.06)

    def test_become_healthier(self):
        initial_health = self.simba.health
        self.simba.become_healthier()
        self.assertAlmostEqual(self.simba.health, initial_health * 1.01)

class TestFence(unittest.TestCase):

    def setUp(self):
        self.savana = Fence(area=100, temperature=27, habitat="Savana")
        self.simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")

    def test_add_animal(self):
        self.savana.add_animal(self.simba)
        self.assertIn(self.simba, self.savana.animals)
        self.assertAlmostEqual(self.savana.area, 94)  # 100 - 6 (area of Simba)

    def test_remove_animal(self):
        self.savana.add_animal(self.simba)
        self.savana.remove_animal(self.simba)
        self.assertNotIn(self.simba, self.savana.animals)
        self.assertAlmostEqual(self.savana.area, 100)

    def test_feed_animal(self):
        self.savana.add_animal(self.simba)
        initial_area = self.savana.area
        initial_health = self.simba.health
        self.savana.feed(self.simba)
        self.assertGreater(self.simba.area(), 6)
        self.assertGreater(self.simba.health, initial_health)
        self.assertLess(self.savana.area, initial_area)

class TestZooKeeper(unittest.TestCase):

    def setUp(self):
        self.savana = Fence(area=100, temperature=27, habitat="Savana")
        self.simba = Animal(name="Simba", species="Leone", age=5, height=2, width=3, preferred_habitat="Savana")
        self.zoo_keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")

    def test_add_animal(self):
        self.zoo_keeper.add_animal(self.simba, self.savana)
        self.assertIn(self.simba, self.savana.animals)

    def test_remove_animal(self):
        self.zoo_keeper.add_animal(self.simba, self.savana)
        self.zoo_keeper.remove_animal(self.simba, self.savana)
        self.assertNotIn(self.simba, self.savana.animals)

    def test_feed_animal(self):
        self.zoo_keeper.add_animal(self.simba, self.savana)
        initial_area = self.savana.area
        initial_health = self.simba.health
        self.zoo_keeper.feed(self.simba)
        self.assertGreater(self.simba.area(), 6)
        self.assertGreater(self.simba.health, initial_health)
        self.assertLess(self.savana.area, initial_area)

    def test_clean(self):
        self.zoo_keeper.add_animal(self.simba, self.savana)
        occupied_area = self.zoo_keeper.clean(self.savana)
        self.assertAlmostEqual(occupied_area, 6 / self.savana.area)

class TestZoo(unittest.TestCase):

    def setUp(self):
        self.savana = Fence(area=100, temperature=27, habitat="Savana")
        self.zoo_keeper = ZooKeeper(name="Bardh", surname="Prenkaj", id="PRNBDH95M09Z160W")
        self.zoo = Zoo(fences=[self.savana], zoo_keepers=[self.zoo_keeper])

    def test_describe_zoo(self):
        with self.assertLogs() as log:
            self.zoo.describe_zoo()
            self.assertIn("Guardians:", log.output[0])
            self.assertIn("Fences:", log.output[1])
            
if __name__ == "__main__":
    unittest.main()