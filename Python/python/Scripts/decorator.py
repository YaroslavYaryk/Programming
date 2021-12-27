import random
import datetime


def time_now(funk):
    def whipper():
        start = datetime.datetime.now()
        result = funk()
        print(datetime.datetime.now() - start)
        return result

    return whipper


@time_now
def array1():
    sum = 0
    for i in range(10000):
        sum += random.randint(10, 20)
    return sum


@time_now
def array2():
    arr = []
    for i in range(10000):
        arr.append(random.randint(10,20))


    return arr

array1()
array2()


