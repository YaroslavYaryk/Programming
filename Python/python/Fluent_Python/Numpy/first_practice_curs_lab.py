import numpy as np
from time import perf_counter

array = np.array([34,21,32,41,25,12,42,43,14,31,54,45,52,42,23,33,15,51,31,35,21,52,33,13,23])
array.resize(5,5)
a = array.tolist()

def funk(a):
    start = a[0][0]
    des = start//10
    od = start%10

    strt = perf_counter()
    while a[des-1][ od-1] != des*10 + od:
        start = a[des-1][ od-1]
        des = start//10
        od = start%10
        if perf_counter() - strt > 1:
            print("there is no such element")
            break
        

    else:
        print(a[des-1][ od-1])    


a = np.ones((5,5), dtype= np.int8)
b = np.ones((5,5), dtype= np.int8)
a= np.triu(a)
b = np.tril(b)
print(a+b)
# print(np.triu(a))
