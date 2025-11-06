class Shape:
    def __init__(self, x=0, y=0):
        # spara positionen internt
        self._x = x 
        self._y = y

    @property
    def x(self):
        return self._x # readable x_ value

    @property
    def y(self):
        return self._y # readable y_ value

    
    
    def __str__(self):
        return f"shape at ({self._x}, {self._y})"



    def __repr__(self): # show how the shape appears in code
        return f"shape({self._x}, {self._y})"


    def translate (self, dx, dy): # check that dx and dy are numbers
        if not isinstance(dx, (int, float)):  # if dx is not a number, stop and give error message
            raise TypeError("dx must be a number")

        elif not isinstance(dy, (int, float)): # if dy is not a number, stop and give error message
            raise TypeError("dy must be a number")

        self._x += dx # update x and y by dx och dy
        self._y += dy



    # comparison operators

    def __eq__(self, other): # check if two shapes are equal
        return (self.x == other.x) and (self.y == other.y) # compare x and y values 
    
    def __lt__(self, other): # check if one shape is less than another
        return (self.x < self.x) and (other.y < other.y) # compare x and y values

    def __ge__(self, other):
        return (self.x >= other.x) and (self.y >= other.y) # check if one shape is greater than or equal to another

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y) # check if one shape is greater than another

    def __le__(self, other):
        return (self.x <= other.x) and (self.y <= other.y) # check if one shape is less than or equal to another







    
