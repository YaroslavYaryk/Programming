from unicodedata import name

a = {1,2,3,4,5,6,7}
b = {1,2,3,4,5,6,7}

((a & b)) # обєднання 
((a | b)) # перетин
((a - b)) # різниця

# (a.pop())
# (a.pop())
# a.add(123)
# a.add(122)
# a.add(121)
# a.discard(123)
# a.discard(122)
# a.discard(121)
a = a.union([1,2,3], [2,99,4], [3,4,5])

print(a)

c = frozenset(range(10)) #unchangeble set of ranges 10 

k = {i for i in range(10) if i % 2 == 0}
# print(k)

d = {chr(i) for i in range(32,256) if "SIGN" in name(chr(i), "") }
# print(d)
