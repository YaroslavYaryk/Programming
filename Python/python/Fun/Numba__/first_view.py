from time import time, sleep
from numba import njit

@njit
def f():
    l = []
    for x in range(10):
        for y in range(10000):
            for z in range(10000):
                if (z + x + y ) / 10 == x:
                    l.append(x)
        print(x)
    return l

start = time()
f()
print(f"time is {round(time() - start, 2)} seconds")                