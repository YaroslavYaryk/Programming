class Python(object):
    __slots__ = ("_x", "_y")

    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    @property
    def funk(self):
        return self._x, self._y

    @funk.setter
    def funk(self,x,y):
        self._x = x
        self._y = y        



py1 = Python(11,12)
print(py1.funk)
