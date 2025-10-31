from shape import Shape
from math import pi

class Circle(Shape):
    def __init__ (self,x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius


    @property
    def radius(self):
        return self.radius

    @property
    def area(self):
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius