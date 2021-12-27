from array import array
import reprlib
import math
import numbers
from functools import reduce
import operator

class Vector():

    typecode = "d"
    
    def __init__(self, component):

        self.__components = array(self.typecode, component)

    def __repr__(self):
        components = reprlib.repr(self.__components)
        components = components[components.find("["): -1 ]
        return f"Vector({components})"


    def __len__(self):
        return len(self.__components)

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        for a, b in zip(self,other):
            if a != b:
                return False
        return True  

    def __eq__(self, other):
        return len(self) == len(other) and all((a==b) for a,b in zip(self,other))
                               

    def __hash__(self):
        hashes = map(hash, self.__components)
        return  reduce(operator.xor, hashes)   


    def  __getitem__(self, index):  
        cls = type(self)
        if isinstance(index, slice):
            return cls(self.__components[index])   
        elif isinstance(index, numbers.Integral):
            return self.__components[index]
        else:
            msg = f"{cls.__name__} index must be integer"
            raise TypeError(msg)


    shortcut_names = "xyzt"
    def __getattr__(self, value):

        cls = type(self)

        if len(value) == 1:
            pos = cls.shortcut_names.find(value)
            if  0<= pos < len(self.__components):
                return self.__components[pos]
            raise AttributeError(f"{cls.__name__} has no attribute {value}")    

    def __setattr__(self, name, value):

        cls = type(self)
        if name in cls.shortcut_names:
            error = f"readonly attribute {name}"
        elif name.islower():
            error = f"cant set attrebutes 'a' to 'z' in {cls.__name__}"
        else:
            error = ""

        if error:
            raise AttributeError(error)

        super().__setattr__(name, value)         

            

obj = Vector([1,2,3,2,1.2])
obj2 = Vector([1,2,3,2,1.2])

print(obj == obj2)
print(hash(obj))
print(hash(obj2))

# print(obj)        
# print(obj[1:-1])
        