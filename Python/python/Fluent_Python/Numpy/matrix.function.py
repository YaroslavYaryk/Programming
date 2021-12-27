import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9])
a.resize(3,3)
print(a)
b = np.eye(5, dtype= np.int8) # main diagon is 1, everything = 0
# print(b, "\n")
 

# a = np.zeros((5,5), dtype= np.int8) #each element is zero (ones - everything is 1)
# print(a)

b = np.diag([1,2,3,4,]) # # main diagonal contains element between brackets
# print(b)

c = np.tri(5) # diagonal and under diagonal are 1
# print(c)

print(np.tril(a)) #make it matrig of triangle view ABOVE main diagon zeros
print(np.triu(a)) #make it matrig of triangle view UNDER main diagon zeros
