import numpy as np  
 
data = [1,2,3,4,5,6,7,8,9,10] #all elements of array have to be the same type

arr = np.array(data, dtype=np.float64) # array of floats

print(arr)
# print(arr.shape)
# print(arr.dtype)
# print(arr.ndim)

arr2 = arr.astype(np.int64) #convert all elements to int
print(arr2)