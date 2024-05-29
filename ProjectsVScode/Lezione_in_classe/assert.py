i:int = 1


assert i == 0, f"the value must be equal to 0 instead is {i}"

import unittest
from 
class Calcu:
    
    def __init__(self, a: int, b: float) -> None:
        self.a:float = a
        self.b:float = b
        
    def get_sum(self):
        return self.a + self.b 
    
    def get_difference(self):
        return self.a - self.b 
    
    def get_product(self):
        return self.a * self.b 
    
    def get_quotient(self):
        return self.a / self.b 