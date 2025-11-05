class Shape:
    def __init__(self, x=0, y=0):
        # spara positionen internt
        self._x = x 
        self._y = y

    @property
    def x(self):
        return self._x # läsbart x_värde

    @property
    def y(self):
        return self._y # läsbart y_värde

    
    
    def __str__(self):
        return f"shape at ({self._x}, {self._y})"



    def __repr__(self): # visa hur formen ser ut i koden 
        return f"shape({self._x}, {self._y})"


    def translate (self, dx, dy): # kolla att dx och dy är nummer
        if not isinstance(dx, (int, float)):  # om dx inte är ett nummer, stoppa och ge felmeddelande
            raise TypeError("dx must be a number")

        elif not isinstance(dy, (int, float)): # om dy inte är ett nummer, stoppa och ge felmeddelande
            raise TypeError("dy must be a number")

        self._x += dx # uppdatera x och y med dx och dy
        self._y += dy



    # comparison operators

    def __eq__(self, other): # kolla om två former är lika
        return (self._x == other._x) and (self._y == other._y) # jämför x och y värdena
    
    def __lt__(self, other): # kolla om en form är mindre än en annan
        return (self._x < self._y) and (other._x < other._y) # jämför x och y värdena som tuples

    def __ge__(self, other):
        return (self._x >= other._x) and (self._y >= other._y) # kolla om en form är större än eller lika med en annan

    def __gt__(self, other):
        return (self._x > other._x) and (self._y > other._y) # kolla om en form är större än en annan

    def __le__(self, other):
        return (self._x <= other._x) and (self._y <= other._y) # kolla om en form är mindre än eller lika med en annan




    

    



    def plot(self, ax):
        pass





    
