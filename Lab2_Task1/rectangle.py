from shape import Shape 

class Rectangle(Shape):
    def __init__ (self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        self._width = width
        self._height = height



    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number")
        elif value <= 0:
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
    def area(self):
        return self._width * self._height



    @property
    def perimeter(self):
        return 2 * (self._width + self._height)

    def __str__(self):
        return f"Rectangle: width={self._width}, height={self._height}, x={self._x}, y={self._y}"

    def __repr__(self):
        return f"Rectangle ({self._x}, {self._y} with width {self._width} and height {self._height})"



      



