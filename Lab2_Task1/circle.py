from shape import Shape # Import the Shape class from shape.py
from math import pi     # Import the pi constant from the math library 

class Circle(Shape): # Creat a Circle class that inherits from Shape class
    def __init__ (self,x=0, y=0, radius=1): # 
        super().__init__(x, y)
        self._radius = radius # use the radius setter to set the radius attribute


    @property
    def radius(self):# getter for the radius attribute
        return self._radius # return the private radius attribute

    @radius.setter 
    def radius(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Radius must be a number")
        elif value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value


    @property 
    def area(self): # Calculates the area of the circle
        return pi * (self.radius ** 2) # Use the radius attribute to calculate the area
        

    @property
    def perimeter(self): # Calculates the perimeter of the circle
        return 2 * pi * self.radius # Use the radius attribute to calculate the perimeter

    # comparison operators

    def __eq__(self, other): # Check if two shapes are equal
        return self.area == other.area # compare area values
    
    def __lt__(self, other): # check if one shape is less than another
        return self.area < other.area # compare area values

    def __ge__(self, other): # check if one shape is greater than or equal to another
        return self.area >= other.area

    def __gt__(self, other): # check if one shape is greater than another
        return self.area > other.area 

    def __le__(self, other): # check if one shape is less than or equal to another
        return self.area <= other.area

    def is_unit_circle(self): # check if the circle is en enhetscircel
        return self.radius == 1 and self.x == 0 and self.y == 0 

    
    def __str__(self): # show the circle's attributes as a string
        return f"Circle: radius={self._radius}, x={self._x}, y={self._y}"

    def __repr__(self): # show how the circle appears in code
        return f"Circle ({self._x}, {self._y} with radius {self._radius})"


circle_1= Circle (0, 0, 1)
circle_2= Circle (2, -1, 1) 





