from abc import ABC, abstractmethod

"""Create an abstract class Shape with an abstract method area and another abstract method perimeter.
Then, create two subclasses Circle and Rectangle that implement the area and perimeter methods."""


class Shape(ABC):
    def __init__(self,area:float,perimeter:float) -> None:
        super().__init__()

        self.area:float = area
        self.perimeter:float = perimeter

    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius:float) -> None:
        self.radius = radius

    def area (self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
# Creazione di un cerchio con raggio 5
circle = Circle(5)
print("Area del cerchio:", circle.area())
print("Perimetro del cerchio:", circle.perimeter())

# Creazione di un rettangolo con lunghezza 4 e larghezza 6
rectangle = Rectangle(4, 6)
print("Area del rettangolo:", rectangle.area())
print("Perimetro del rettangolo:", rectangle.perimeter())

