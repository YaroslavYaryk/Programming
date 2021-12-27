import diamond_one
import numbers


def print_mro(cls):

    print(", ".join(c.__name__ for c in cls.__mro__))

print_mro(diamond_one.D)    
print_mro(numbers.Integral)    
