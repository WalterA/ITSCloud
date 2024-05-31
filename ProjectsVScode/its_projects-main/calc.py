# i: int = 0

# assert i == 0, f"The value must be equal to 0 instead is {i}!"


# def check_sqrt(func, input, result):
    
#     n = func(input)
    
#     assert n == result, f"Error the expected value is: {result} Your function returns: {n}"
    
    
    
# def constant(input) -> int:
    
#     return -1


# from math import sqrt

# check_sqrt(sqrt, 4, 2)
# check_sqrt(sqrt, 9, 2)
# check_sqrt(sqrt, 5, sqrt(5))
# check_sqrt(sqrt, 16, 4)



class Calculations:
    
    def __init__(self, a: float, b: float) -> None:
        self.a: float = a
        self.b: float = b
        
    def get_sum(self):
        return self.a + self.b
    
    def get_difference(self):
        return self.a - self.b
    
    def get_product(self):
        return self.a * self.b
    
    def get_quotient(self):
        return self.a / self.b