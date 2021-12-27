from operator import methodcaller, mul, add
from functools import partial

s = "hello world and everybody"
uppercase = methodcaller("upper")
hiphenate = methodcaller("replace", " ", " - " )

# print(uppercase(s))
# print(hiphenate(s))

# a = list(map(lambda x: x+3, range(1,10)))
# # print(a)

# triple = partial(mul,3) #it works like a function do 
#we can use it in map-function
# print(triple(5))
# a = list(map(triple,range(1,10)))
# print(a)
a = list(map(int, input().split()))
print(a)