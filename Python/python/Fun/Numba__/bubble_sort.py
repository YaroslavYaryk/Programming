import numpy as np
import time 
import random
from numba import njit

@njit
def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                
A = np.arange(5000,0, -1)               
                
start = time.time()
bubbleSort(A)
print(f"time is {time.time() - start} second")    
                  
                