import numpy as np

a = np.random.randint(1,100, size = 9).reshape(3,3)
b = np.random.randint(1,100, size = 9).reshape(3,3)
(a, "\n\n" , b, "\n\n", a+b)

c = np.hstack([a, b]).T
d = np.vstack([a,b])
e = np.amax(c+d, axis = 0)
(c, "\n\n" , d, "\n\n", c+d)
# print(e)
abb = np.array([1,2,3,4,5,7,76,5,4])
# print(abb)
np.random.shuffle(abb)
# print(abb)

def is_true(arr):
    arr1 = sorted(arr)
    return  (arr1 == arr).all()

def arrr(arr):
    oper = 0
    while not is_true(arr):
        np.random.shuffle(arr)
        oper += 1
    else:
        return f"Got it {arr}, {oper} operations"    


arr = np.random.randint(1,10, size = 8)
print(arrr(arr))


        
