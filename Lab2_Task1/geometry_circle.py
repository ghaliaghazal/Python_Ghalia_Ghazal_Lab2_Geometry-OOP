from shape import Shape
from math import pi

class Circle(Shape):
    def __init__ (self,x=0, y=0, radius=1):
        super().__init__(x, y)
        self.radius = radius



    @property
    def radius(self):
        return self._radius # returnerar det privata radie-attributet

    @radius.setter
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        elif value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value


    @property
    def area(self):
        return pi * (self.radius ** 2)

    @property
    def perimeter(self):
        return 2 * pi * self.radius


circle_1= Circle()
print(circle_1.area)
print(circle_1.perimeter)

circle_2= Circle()
print(circle_2.area)
print(circle_2.perimeter)


