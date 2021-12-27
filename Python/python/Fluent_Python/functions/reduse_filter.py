from functools import reduce
from operator import add


c = reduce(add, range(1,11))
print(c)    
print(sum(range(1,11)))

def filtered(n):
    if n %2 == 0:
        return True
    return False

print(list(filter((lambda x: x%2 == 0) , range(1,11))))