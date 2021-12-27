import time
"""this decorator create the file and write there 
the files that we write in function we can upgrate this decorator in order to write
the imformation , like, 
function_name {},  text {}, it's pretty eazy
but it's important not to forget about "wraps" in functools library
to save our real function_name and __doc__ """
def add_file(funk):

    def Wrapper(*args, **kwargs):
        print("start downloading")
        for i in range(5):
            print("downloading...")
            time.sleep(1)
        with open("log.txt", "w") as f:
            f.write(funk(*args, **kwargs))
        time.sleep(3)
        print("finish downloading")
    return Wrapper

@add_file
def Someth_writer(text):
    if isinstance(text, str):

        if len(text) <= 100:
            return text
        else:
            raise OutOfMemoryError
    else:
        raise ValueError("must be string")

Someth_writer("hello world")
with open("log.txt", "r") as f:
    print(f.read())

"""this decorator like decorator Property "getter" in classes it warks
the same way"""

class Property(object):

    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obg_type):
        if obj is None:
            return self
        else:
            return self.getter(obj)


class Point(object):

    def __init__(self,name, age):
        self.name = name
        self.age = age

    @Property
    def printa(self):
        return self.name, self.age

person = Point("Yaroslav", 17)
print(person.printa)

"""like i wrote as function the same work"""

class Timer(object):

    def __init__(self, funk):
        self.funk = funk

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.funk(*args, **kwargs)
        print(time.time() - start)
        return result

@Timer
def factorial(x):
    storage = 1
    for i in range(1,x+1):
        storage *= i
    time.sleep(0.0001)
    return storage

print(factorial(50))

"""the same as i wrote earlier to remember the operations what we've already done 
in order not to waste our time """

class Lru_cache(object):

    def __init__(self, funk):
        self.funk = funk
        self.storage = {}

    def __call__(self, *args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in self.storage:
            self.storage[key] = self.funk(*args, **kwargs)
        return self.storage[key]


start = time.time()


@Lru_cache
def Fibo(x):
    return Fibo(x-1) + Fibo(x-2) if x > 1 else x


print(Fibo(50))
print(f"Time - {time.time() - start}")


# Decorator with arguments

class Decorator(object):

    def __init__(self, name):
        self.name = name

    def __call__(self, funk):

        def wrapper(*args, **kwargs):
            print("work with decorator", self.name)
            print("start")
            funk(*args, **kwargs)
            print("end")
        return wrapper

@Decorator("Pringlton")
def say_hello(name):
    print("hello", name)                


say_hello("Yaroslav")    