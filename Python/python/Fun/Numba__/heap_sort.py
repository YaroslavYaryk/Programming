import numpy as np
import time 
import random
from numba import njit

@njit

def heapify(A, heap_size, root_index):  
    #the largest element is root_index
    largest = root_index
    left_child = (2 * root_index) 
    right_child = (2 * root_index) + 1 

    #if left_child is avaluable  and bigger than largest then
    # vhange largest
    if left_child < heap_size and A[left_child] > A[largest]:
        largest = left_child

    #if right_child is avaluable  and bigger than largest then
    # change largest
    if right_child < heap_size and A[right_child] > A[largest]:
        largest = right_child

    #if largest is not equal to root_index, swap them
    if largest != root_index:
        A[root_index], A[largest] = A[largest], A[root_index]
        # Heapify the new root element to ensure it's the largest
        heapify(A, heap_size, largest)

@njit
def heap_sort(A): 

    n = len(A)

    # Build a maxheap.  
    #Since last parent will be at ((n//2)-1) we can start at that location. 
    for i in range((n//2)-1, -1, -1):
        heapify(A, n, i)

    #swap elements one by one 
    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

            

A = np.arange(500000,0, -1)
# print(A)
# B = list(range(1, 5001))
# C = list(range(5000, -1, -1))          


start = time.time()
heap_sort(A)
print(f"time is {time.time() - start} second")    
  
        
  