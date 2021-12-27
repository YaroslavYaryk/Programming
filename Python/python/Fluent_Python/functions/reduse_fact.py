from functools import reduce
from operator import mul, itemgetter

def factorial(x):
    return reduce(mul, range(1,x+1))

print(factorial(4)) 

a = [('hello', 1, 20020),("world", 121, 10202),("and", 212, 10204),("everybody", 123, 12345)]

for elem in sorted(a, key = lambda x: len(x[0])):
    print(elem)
print()

cc = itemgetter(0,1) #allow us to print only first and second value
for elem in a:
    print(cc(elem))