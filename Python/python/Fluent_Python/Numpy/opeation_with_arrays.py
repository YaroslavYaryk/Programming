import numpy as np

a = np.arange(1,10)
b = np.arange(11,20)
a +=b
a *= b
a -= b**2
a //=b

c = np.vstack([a,b])
# print(c)

c = np.ones((4,4), dtype= np.int16)
d = np.arange(16).reshape(4,4)
d**=2

c+=d
# print(c)

arr1 = np.array([1,2,3,4])
arr1 = np.append(arr1,12)
print(arr1)