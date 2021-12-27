from functools import  lru_cache
import sys

sys.setrecursionlimit(10**6)

@lru_cache()
def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)    


# print(fibo(10))        

# @lru_cache()
def factorial(n):
    if n ==0:
        return 1
    else:
        return factorial(n-1) * n    

print(factorial(2417))