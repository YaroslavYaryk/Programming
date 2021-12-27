import math
import time
from numba import njit, prange

@njit(fastmath = True)
def is_simple(num) :
    if num == 2:
        return True
    if num <= 1 or not num % 2:
        return False
    for i in range (3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

@njit(fastmath = True)
def run_program():
    for i in range(10000000):
        is_simple(i)
        

if __name__ == "__main__":        
    start = time.time()
    run_program()
    print(f"time is {round(time.time() - start, 2)} second")    
    