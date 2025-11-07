from shape import Shape 

class Rectangle(Shape): # creat a Rectangle class that inherits from Shape class
    def __init__ (self, x=0, y=0, width=1, height=1): 
        super().__init__(x, y)
        self.width = width
        self.height = height



    @property
    def width(self): # getter for the width attribute
        return self._width # returns the private width attribute
     
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)): # if value is not a number, stop and give error message
            raise TypeError("Width must be a number")
        elif value <= 0:     # if value is not positive, stop and give error message
            raise ValueError("Width must be positive")
        self._width = value 

    
    @property
    def height(self): 
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be a number")
        elif value <= 0:
            raise ValueError("height must be positive")
        self._height = value

    
    @property
    def area(self): # calculates the area of the rectangle
        return self._width * self._height

    @property
    def perimeter(self): # calculates the perimeter of the rectangle
        return 2 * (self._width + self._height)

    def is_square(self): # check if the rectangle is a square and return True or False
        return self._width == self._height

    def __repr__(self): # show the rectangle's attributes as a string
        return f"Rectangle: width={self._width}, height={self._height}, x={self._x}, y={self._y}"  

    def __str__(self): # show how the rectangle appears in code
        return f"Rectangle at ({self._x}, {self._y} with width {self._width} and height {self._height})"
