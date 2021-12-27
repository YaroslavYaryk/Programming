import numpy as np
import time 
import random
from numba import njit

@njit
def stoogesort(arr, l, h):
    if l >= h:
        return
   
    # If first element is smaller
    # than last,swap them
    if arr[l]>arr[h]:
        t = arr[l]
        arr[l] = arr[h]
        arr[h] = t
   
    # If there are more than 2 elements in
    # the array
    if h-l+1 > 2:
        t = (int)((h-l+1)/3)
   
        # Recursively sort first 2/3 elements
        stoogesort(arr, l, (h-t))
   
        # Recursively sort last 2/3 elements
        stoogesort(arr, l+t, (h))
   
        # Recursively sort first 2/3 elements
        # again to confirm
        stoogesort(arr, l, (h-t))
        
        
        
A = np.arange(1000,0, -1)               
            
n = len(A)
                
start = time.time()
stoogesort(A, 0, n-1)
print(f"time is {time.time() - start} second")           