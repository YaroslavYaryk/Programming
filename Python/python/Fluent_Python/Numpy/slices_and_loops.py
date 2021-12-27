import numpy as np

a = np.arange(1,26).reshape(5,5)
 
b = a[0:, 1:] #everything except first column
b = a[4:,4:] #last element
b = a[:,:] #whole matrix
# print(b)

d = np.ones((5,5,5), dtype=np.int8)
c = d[4, ...] #forth row and everything (... means we get everything(the same as (4,:,:)))
#if we have two ":" or more it should ti use this one
c = np.tril(c)
c = d[1,1,...]#but we can use (...) whn we have only one ":"
print(c)


k = np.arange(10)
d = k[k>5] #get each element larger than 5 , incredible
d = k[[1,2,3,0]] #get element indexes those ore in breackets
print(d)

s = np.arange(1,11)
s[0:4] = [12,3,2,3] #change slices
s[[1,2,3,4]] = [-1,-2,-3,-4]
# print(s)

p = np.arange(9).reshape(3,3)
print(p)
k = p[[0,1],[1,2]] #we get first and second row andtake from there second and third element 
print(k)
