class shape:
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

    
    @property
    def __str__(self):
        return f"shape at ({self._x}, {self._y})"



    @property
    def __repr__(self):
        return f"shape({self._x}, {self._y})"

    @property
    def move(self, dx, dy):
        self._x += dx
        self._y += dy

    