from random import sample, choice
import time

a = sample(range(1,11), 10)
b = sample(range(1,10001), 10000)

def funk(arr, num):
    array = [0] * num
    pos = 0
    while  pos < len(array):
        array[pos] = choice(arr)
        if array[pos]%2==0:
            pos+=2
            array.insert(pos-2,0)
        else:
            pos+=1
    return array        



def main1():
    start = time.perf_counter()
    funk(a, 10)
    print(f" time of inserting array - {round(time.perf_counter() - start,7)}")

def main2():
    start = time.perf_counter()
    funk(b, 10000)
    print(f" time of inserting array - {round(time.perf_counter() - start,7)}")



if __name__ == '__main__':
    main1()
    main2()


