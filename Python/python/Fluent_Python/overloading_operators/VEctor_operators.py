import itertools
import reprlib
import math
import numbers

class Vector(object):

    typecode = "d"

    def __init__(self, component):

        self.__components = list(component)

    def __repr__(self):

        return f"Vector{tuple(c for c in self.__components)}"

    def __iter__(self):
        return iter(self.__components)   

    def __add__(self, other):
        if isinstance(other, Vector):
            pairs = itertools.zip_longest(self,other, fillvalue = 0)
            return Vector(a + b for a,b in pairs)     
        
        raise ValueError("Wrong type of operands")

    def __radd__(self, other):
        return self + other

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)    


    def __abs__(self) -> float:
        return math.sqrt(sum(a*a for a in self))

    def __mul__(self, other):
        if isinstance(other, Vector):
            pairs = itertools.zip_longest(self,other, fillvalue = 0)
            return Vector(a * b for a,b in pairs) 
        elif isinstance(other,numbers.Real) :
            return Vector(a * other for a in self)
        else:
            raise ValueError("Wrong type of operands")                                  

    def __rmul__(self, other):
        return self * other

    def __sub__(self, other):
        if isinstance(other, Vector):
            pairs = itertools.zip_longest(self,other, fillvalue = 0)
            return Vector(a - b for a,b in pairs)
        raise ValueError("Wrong type of operands")              

    def __rsub__(self, other):
        return self * other

    def __pow__(self, value):
        if isinstance(value,numbers.Real) :
            return Vector(a ** value for a in self) 
    def __truediv__(self, other):
        if isinstance(other, Vector):
            pairs = itertools.zip_longest(self,other, fillvalue = 0)
            return Vector(a / b for a,b in pairs) 
        elif isinstance(other,numbers.Real) :
            return Vector(a / other for a in self)
        else:
            raise ValueError("Wrong type of operands")

    def __len__(self):
        return len(self.__components)        

    def __matmul__(self, other):
        if isinstance(other, Vector):
            pairs = zip(self, other)
            return sum (a * b for a,b in pairs) 
        elif isinstance(other,numbers.Real) :
            return sum(a * other for a in self)
        else:
            raise ValueError("Wrong type of operands")

    def __rmatmul__(self, other):
        return self @ other
        

    def __eq__(self, other):
        if isinstance(other, Vector):
            return (len(self) == len(other)) and all(a == b for a, b in zip(self, other)) 
        return NotImplemented    

    def __ne__(self, other):
        res = self == other
        if res is NotImplemented:
            return NotImplemented
        return not res    


vect1 = Vector([1,2])
vect2 = Vector([4,8])

print(id(vect1))
vect1 += vect2

print(id(vect1))

