import time
from functools import wraps
from functools import lru_cache, update_wrapper


def timer(n):
    if n == 3:
        exit()

    def wrapper(funk):
        """we use this decorator to save our real fumction __name__ and __doc__
        without it we get "name of function ==  second"
        but with this one we"ll get "name of function ==  factorial"
        """
        start = time.time()
        @wraps(funk)
        def second(*args, **kwargs):
            
            result = funk(*args, **kwargs)
            end = time.time() - start
            
            return result
        # print(end)    
        return second
    return wrapper


"""
we use this decorator to remember our last operation that's  useful when we wanna find n-element of Fibonacci list, 
now the function doesn't remember all the operations to find 100 number of Fibonacci list we have to use 101 operations
instead of a couple of milions 
"""


def Lru_cache(funk):
    storage = {}

    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in storage:
            storage[key] = funk(*args, **kwargs)
        return storage[key]
    return wrapper


@Lru_cache
def Fibo(n):
    return Fibo(n-1) + Fibo(n-2) if n > 1 else n


print(Fibo(100))


# @timer(3)
@Lru_cache
def factorial(x):
    storage = {}
    if x not in storage:
        if x == 0:
            storage[x] = 1
        else:
            storage[x] = x * factorial(x-1)
    return storage[x]


print(factorial(100))
print("name of function == ", factorial.__name__)


#  Decorators in class
class Decorator(object):

    """
    "update_wrapper is the same as decorator "@wraps" when we used it as function
    fist argument is "where" , second "from"
    """

    def __init__(self, funk):
        update_wrapper(self, funk)
        self.__funk = funk

    def __call__(self, *args, **kwargs):
        return self.__funk(*args, **kwargs)


@Decorator
@Lru_cache
def factorial(x):
    storage = {}
    if x not in storage:
        if x == 0:
            storage[x] = 1
        else:
            storage[x] = x * factorial(x-1)
    return storage[x]


print(factorial(5))
print(factorial.__name__)
