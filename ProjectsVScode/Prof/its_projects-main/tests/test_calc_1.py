import unittest
from src.calc import Calculations


class TestCalc(unittest.TestCase):
    
    def test_sum(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_sum()
        self.assertEqual(result, 4, msg=f"Error Test Failed the goal was 5 the function returned {result}")
        
    def test_prod(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_product()
        self.assertEqual(result, 6, msg=f"Error Test Failed the goal was 6 the function returned {result}")
                
    def test_diff(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_difference()
        self.assertEqual(result, -1, msg=f"Error Test Failed the goal was -1 the function returned {result}")

    def test_div(self):
        
        calc_1 = Calculations(a=2, b=3)
        result = calc_1.get_quotient()
        self.assertEqual(result, 2/3, msg=f"Error Test Failed the goal was {2/3} the function returned {result}")
        
if __name__ == "__main__":
    
    unittest.main()
