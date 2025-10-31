from shape import Shape 

class Rectangle(Shape):
    def __init__ (self, x=0, y=0, width=1, height=1):
        super().__init__(x, y)
        self.width = width
        self.height = height


    @property
    def width(self):
        return self._width

    
    @property
    def height(self):
        return self._height

    
    @property
    def area(self):
        return self.width * self.height



    @property
    def perimeter(self):
        return 2 * (self.width + self.height)

