from shape import Shape 

class Rectangle(Shape):
    def __init__ (self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        self.width = width
        self.height = height


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
            raise TypeError("Height must be a number")
        elif value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    
    @property
    def area(self):
        return self.width * self.height



    @property
    def perimeter(self):
        return 2 * (self.width + self.height)


rektangel_1= Rectangle(0, 0, 2, 2)
print(rektangel_1.area)
print(rektangel_1.perimeter)



