from shape import Shape # importerar Shape klassen från shape.py
from math import pi     # importerar pi konstanten från math-biblioteket
import numpy as np  # importerar numpy biblioteket för matematiska operationer

class Circle(Shape): # skapa en Circle klassen som ärver från Shape klassen
    def __init__ (self,x=0, y=0, radius=1): # 
        super().__init__(x, y)
        self.radius = radius # använder setter för att sätta radie attributet



    @property
    def radius(self):# getter för radie attributet
        return self._radius # returnerar det privata radie attributet

    @radius.setter 
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        elif value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value


    @property 
    def area(self): # beräknar arean av cirkeln
        return pi * (self.radius ** 2) # använder radie attributet för att beräkna arean
        

    @property
    def perimeter(self): # beräknar omkretsen av cirkeln
        return 2 * pi * self.radius # använder radie attributet för att beräkna omkretsen





import matplotlib.pyplot as plt # importerar matplotlib biblioteket för att rita cirkeln

circle_1 = plt.Circle((0,0), 1, color='blue') # skapar en cirkel med centrum i (0,0) och radie 1
ax.set_xlim() # sätter x-axelns gränser
ax.set_ylim() # sätter y-axelns gränser

