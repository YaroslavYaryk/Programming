import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9], dtype=np.int64)
a = arr[[True,False,False, False, False, True, True, True, False]]
# print(a)# print elements if inedx is True

arr.resize(3,3)#makes it as matrix (3,3)
# print(arr)

c = np.array([1,2,3,4,5,6,7,9,8])
# c.resize(3,3)
# print(c)

e = np.array([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
e.resize(5,5)
print(e)


d = c[1:4]
print(d)