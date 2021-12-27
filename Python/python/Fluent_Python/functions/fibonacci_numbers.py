from functools import lru_cache

@lru_cache
def fib_nums(n):
    """find n-elem of Fibonacci numbers"""
    if n == 0: 
        return 0

    if n == 1:
        return 1
    else:
        return fib_nums(n-1) + fib_nums(n-2)    


a = list(map(fib_nums, range(5,11)))

# print(a)

# print(fib_nums(100))        
# print(fib_nums.__doc__)

a = ["hello", "world", "AND", "everybody"]
# print(sorted(a, key = str.lower))

print(dir(fib_nums))