from shape import Shape 

class Rectangle(Shape): # skapa en Rectangle klassen som ärver från Shape klassen
    def __init__ (self, x=0, y=0, width=1, height=1): # 
        super().__init__(x, y)
        self._width = width
        self._height = height



    @property
    def width(self): # getter för width attributet
        return self._width # returnerar det privata width attributet
     
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)): # om value inte är ett nummer, stoppa och ge felmeddelande
            raise TypeError("Width must be a number")
        elif value <= 0:     # om value är mindre än eller lika med 0, stoppa och ge felmeddelande
            raise ValueError("Width must be positive")
        self._width = value 

    
    @property
    def height(self): # 
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("height must be a number")
        elif value <= 0:
            raise ValueError("height must be positive")
        self._height = value

    
    @property
    def area(self): # beräknar arean av rektangeln
        return self._width * self._height



    @property
    def perimeter(self): # beräknar omkretsen av rektangeln
        return 2 * (self._width + self._height)

    def is_square(self):
        return self._width == self._height

    def __str__(self): # visa rektangelns attribut som en sträng
        return f"Rectangle: width={self._width}, height={self._height}, x={self._x}, y={self._y}" # 

    def __repr__(self): # visa hur rektangeln ser ut i koden
        return f"Rectangle ({self._x}, {self._y} with width {self._width} and height {self._height})"



      



