import time
import random
import prettytable
import sys
from numba import njit

sys.setrecursionlimit(10**6)

start1 = time.perf_counter()
def pow_reccursive(num,degree) -> int:
    if degree == 0:
       return num
    else:
        return (num* pow_reccursive(num, degree-1))

pow_reccursive(20,2416)
finish1 = round(time.perf_counter() - start1, 7)

start2 = time.perf_counter()
def pow_simple(num, degree) -> int:
    result = num

    for i in range(1,degree):
        result *= num

    return result

(pow_simple(20,2417))
finish2 = round(time.perf_counter() - start2, 7)



def prettytable1():      
    pretty_one = prettytable.PrettyTable()
    pretty_one.field_names = ["type", "time"]
    pretty_one.add_row(["Reccursive", finish1])
    pretty_one.add_row(["Noneccursive", finish2])

    print(pretty_one.get_string())


if __name__ == "__main__":
    prettytable1()
