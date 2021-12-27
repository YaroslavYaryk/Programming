import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([7, 6, 5, 4, 3, 2, 1])
# print("arr1 == arr2") if (arr1 == arr2).all() else print("arr1 != arr2")


arr1 = np.arange(1, 12)
arr2 = np.arange(10, -1, -1)
(np.all(arr1 > 5))  # cheack if all elements of arr1 is more than 5 (False)
(np.any(arr1 == 5))  # cheack if at least one  element of arr1 is equal to  5 (true)

arr1 > arr2
arr1 == arr2
arr1 < arr2

arr1 = np.array([True, False, False, False, True, True, True])
arr2 = np.array([False, False, True, False, False, True, False])


(np.logical_and(arr1, arr2))
(np.logical_or(arr1, arr2))
(np.logical_xor(arr1, arr2))
(np.logical_not(arr1))
(np.logical_not(arr2))

a = np.arange(1, 10).reshape(3, 3)
(a.max())  # the iziest way of finding the larger element
((a.max(axis=0)).max())  # the hardest one
(np.amax(a)) # the same way 
np.amin(a) # find the smallest element



a = [1, 2, 3, -3, -4, -5]

(np.abs(a))  # make abs to all of the elements

(np.argmax(a)) # find index of the largest element
(np.argmin(a)) # find index of the smallest element


arer = np.arange(1,10).reshape(3,3)
(np.sin(arer)) #find sinus   from all elements
(np.cos(arer)) #find cosinus from all elements
(np.tan(arer)) #find tangens from all elements
