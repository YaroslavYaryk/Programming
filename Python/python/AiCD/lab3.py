import time
import random
import prettytable
from numba import njit



class Timer(object):

    def __init__(self, funk):
        self.funk = funk

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        result = self.funk(*args, **kwargs)
        finish = round(time.perf_counter() - start,6)*10**6
        return finish


A = random.sample(range(1,21), 20)
B = list(range(1, 21))
C = list(range(20, -1, -1))


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

@Timer
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


@Timer
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


def prettytable1(funk):      
    pretty_one = prettytable.PrettyTable()
    pretty_one.field_names = ["type", "time"]
    pretty_one.add_row(["Random", funk(A)])
    pretty_one.add_row(["Up", funk(B)])
    pretty_one.add_row(["Down", funk(C)])
    print(pretty_one.get_string())


if __name__ == "__main__":
    print("___________Piramida____________")
    prettytable1(heap_sort)
    print("******************************")
    print("____________Radix______________")
    prettytable1(radix_sort)
