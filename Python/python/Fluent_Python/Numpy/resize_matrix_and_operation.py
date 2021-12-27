import numpy as np

a = np.array([1,1,2,3,4,5,6,7,8])
a.resize(3,3)
a.resize(4,5, refcheck=False) #if in the brackets size bigger than size of mstrix
#and REFCKEK is false we make our matrix this size by adding zeros
# if smoller than matrix size we make ou matrix this size 
# print(a)

c = np.arange(1,10) #its a vector
#we cant transpose it 'cause it has only  one dimension (1 row)
#so we can add 1 more row to is by (c.shape = 1,-1)
c.shape = 1,-1
d = c.T #we get the result
# print(d)

c = np.arange(1,5).reshape(2,2)
# print(c)
d = np.expand_dims(c, axis=0) #add new вiсь to aur matrix, so we change shape of matrix  
# print(d)
d = np.append(d,d, axis=0) #add elements to matrix
# print(d)


d = np.delete(d,0, axis=0) #delete elements to matrix
# print(d)


k = np.array([1,2,3,4,5]) 

k = np.expand_dims(k, axis = -1)
print(k)

