import numpy as np

a = np.ones((3,4,5), dtype=np.int8)

# print(a.shape)

b = a.reshape(2,5,6) # create an array, so we can присвоїти it with our array 

a.resize(2,5,6) #doesnt create new array , if we try присвоїти and print we get NONE

#if we wanna make a copy of array and want to save all the elements we can do like this:

c = np.array([1,2,3,4,5])
d = c #but if we change C , D changes as well

c = np.array([1,2,3,4,5,6])
d = c.view() #better one we make an copy , that independent from main C

c = np.array([1,2,3,4,5,6])
d = c.copy() #or like this


f = np.array([1,2,3,4,5,6,7,8,9,0])
f.shape = -1,2 # we write  -1 as a row because 
#we want it to be  2-col matrix and it'll be len(f) / col rows 
print(f,"\n")

s = np.array([1,2,3,4,5,4])
q = s.reshape(2,-1)
print(q,"\n")
q.shape = -1 #mwke it like a vector (1 row)
q.resize(1, 6) #if we do like this it doesnt make it like a vector it just make 1 row matrix
#we can make sure it when we take a look at print these two prints 

print(q,"\n")
print(s)