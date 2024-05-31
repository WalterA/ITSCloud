import unittest
from unittest import TestCase

from src.bardh_zoo import Zoo,ZooKeeper,Animal,Fence

class testZoo(TestCase):
    
    def setUp(self) -> None:
        self.fences: list[Fence] = []
        self.zk: list[ZooKeeper] = []
        
        self.zoo_1: Zoo = Zoo(self.fences, self.zk)
        self.ZooKeeper_1: ZooKeeper = ZooKeeper("Mario","Rossi","123")
        self.fence_1: Fence = Fence(10000,10.5,"Forest")
        self.animal_1: Animal = Animal("Bob","Cane",23,10.2,5.3,"Forest")
        
        
        
    def test_1(self):
        """controlla che animale troppo grandi non vengono aggiunti alla fence"""
        
        
        ZooKeeper_1: ZooKeeper = ZooKeeper("Mario","Rossi","123")
        fence_1: Fence = Fence(10000,10.5,"Forest")
        animal_1: Animal = Animal("Bob","Cane",23,10.2,5.3,"Forest")
        ZooKeeper_1.add_animal(animal_1,self.fence_1)
        result: int = len(fence_1.animals)
        message:str = f"Error: the "
        
        self.assertEqual(result,0,message)
        
    def test_2(self):
        self.ZooKeeper_1.remove_animal(self.animal_1,self.fence_1)
        result: int = len(self.fence_1.animals)    
        message:str = f"piena"
        
        self.assertAlmostEqual(result, 0 , message)
        
    def test_3(self):
        self.ZooKeeper_1.feed(self.animal_1)
        result = True
        if self.animal_1.health != 100:
            result = True
            return result
        self.assertAlmostEqual(result)
        
    if __name__ == "__main__":
        unittest.main()