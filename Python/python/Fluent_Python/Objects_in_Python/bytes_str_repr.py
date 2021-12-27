
class Vector(object):

    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):
        if isinstance(other, Vector):
            self._x += other._x
            self._y += other._y
        elif isinstance(other,int) or isinstance(other,float):
            self._x += other
            self._y += other
        else:
            raise ValueError("Vrong type of operands")
        return Vector(self._x, self._y)     

    def __iadd__(self, other):
        if isinstance(other, Vector):
            self._x += other._x
            self._y += other._y
        elif isinstance(other,int) or isinstance(other,float):
            self._x += other
            self._y += other
        else:
            raise ValueError("Vrong type of operands")
        return Vector(self._x, self._y)


    def __abs__(self) -> float:
        return (self._x**2 + self._y**2)**0.5

    def __iter__(self):
        return (i for i in (self._x, self._y))  

    def __format__(self, fmt_spec = ""):
        componrnts = (format(c,fmt_spec) for c in self)
        return "({}, {})".format(*componrnts)

    def __hash__(self):
        return hash(self._x) ^ hash(self._y)


    def __eq__(self, other):
        print(tuple(self))
        print(tuple(other))

        return tuple(self) == tuple(other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            self._x *= other._x
            self._y *= other._y
        elif isinstance(other,int) or isinstance(other,float):
            self._x *= other
            self._y *= other
        else:
            raise ValueError("Vrong type of operands") 
        return Vector(self._x, self._y)                                  


    def __imul__(self, other):
        if isinstance(other, Vector):
            self._x *= other._x
            self._y *= other._y
        elif isinstance(other,int) or isinstance(other,float):
            self._x *= other
            self._y *= other
        else:
            raise ValueError("Vrong type of operands") 
        return Vector(self._x, self._y)

vect1 = Vector(1,2)
vect2 = Vector(2.1,3.4)
print(vect1 == vect2)

print(hash(vect1))
print(hash(vect2))


# print(vect1)