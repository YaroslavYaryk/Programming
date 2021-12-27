import numpy as np

a = np.array([1,2,5,4,3,2,2,3,4]).reshape(3,3)
b = np.array([1,2,5,1,2,5,1,2,1]).reshape(3,3)

(np.amax(np.dot(b,a))) # multiply matrix
(np.amax(np.dot(a,b))) # multiply matrix

(a @ b) # multiply matrix the same way

arr1 = np.array([1,2,3,4,5,6,7])
arr2 = np.array([1,2,3,4,5,7,7])

# print(arr1, "\n", arr2)
# print(arr1 @ arr2)

(np.inner(arr1, arr2)) #inner multiply (will be the same if we transport one if the arrays and multiply arr1 @ arr2)
(np.outer(arr1, arr2)) #outer multiply (will be the same if we transport one if the arrays and multiply arr2 @ arr1)

ar1 = np.random.randint(1,10, size = 25).reshape(5,5)
ar2 = np.random.randint(1,10, size = 25).reshape(5,5)
(ar2 @ ar1)


a = np.random.randint(1,10, size = 9).reshape(3,3)
y  = np.random.randint(1,10, size = 3)

print(np.round(np.linalg.solve(a, y))) if np.linalg.matrix_rank(a) == len(y) else print("can't do this")