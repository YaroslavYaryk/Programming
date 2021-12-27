from rich.console import Console
from rich.table import Table
import time 
import random
from numba import njit


@njit
def radix_sort(A:list):
    length = len(str(max(A)))
    rang = len(A)
    for i in range(length):
        B = [[] for k in range(rang)] 
        for x in A:
            figure = x // 10**i % 10 #get figure of some rang`
            B[figure].append(x) #add this one to B array
        A = []
        for k in range(rang):
            A = A + B[k]
            

A = random.sample(range(1,5001), 5000)
# B = list(range(1, 5001))
# C = list(range(5000, -1, -1))          


start = time.time()
radix_sort(A)
print(f"time is {time.time() - start} second")    
  
        
  