from shape import Shape 

class Rectangle(Shape):
    def __init__ (self, x=0, y=0, width=1, length=1):
        super().__init__(x, y)
        self.width = width
        self.length = length



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
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("length must be a number")
        elif value <= 0:
            raise ValueError("length must be positive")
        self._length = value

    
    @property
    def area(self):
        return self.width * self.length



    @property
    def perimeter(self):
        return 2 * (self.width + self.length)






