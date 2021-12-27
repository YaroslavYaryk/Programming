import numpy as np

arr1 = np.array([1,1,2,3,4,5,5,6,6])
arr2 = np.array([6,6,5,5,4,3,2,1,1])
arr1.resize(3,3)
arr2.resize(3,3)
# print(arr1, " \n\n" ,arr2)
arr3 = np.hstack([arr1, arr2]) #union 2 arrays by horisontal
# print(arr3, " \n$0\n")
arr3 = np.vstack([arr1, arr2]) #union 2 arrays by vertical
# print(arr3, " \n$0")

"""

[[1 1 2 6 6 5]
 [3 4 5 5 4 3]
 [5 6 6 2 1 1]]  
$0

[[1 1 2]
 [3 4 5]
 [5 6 6]
 [6 6 5]
 [5 4 3]
 [2 1 1]]"""
 

arr4 = np.array([1,1,2,3,4,5,5,6,6])
arr5 = np.array([6,6,5,5,4,3,2,1,1])
arr6 = np.column_stack([arr4, arr5]) #uniom 2 arrays by column (vertical)[[1 6]
"""
 [[1 6]
 [2 5]
 [3 5]
 [4 4]
 [5 3]
 [5 2]
 [6 1]
 [6 1]]
 """
# print(arr6) 


a = np.r_[1:9, 123 ]  #create an array from diferent arrays betweem brackets
b = np.r_[[(1,2,3)], [(1,2,3)]] #gonna be voubly  shaped array
c = np.r_[1:5] # the same as np.arange(1,5)
# print(b)


e = np.array([1,2,3,4,5,6])
d = np.array_split(e, 2, axis=0)#split array on integer what is into brackets (shape = 1)
d = np.hsplit(e, 2) #the same as previous one but it has default (shape=1)
e.resize(2,3)
k = np.vsplit(e,2)
k = np.hsplit(e,3)

print(k)