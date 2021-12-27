import heapq as hp

def heapsort(iterable):
    h = []

    for value in iterable:
        hp.heappush(h, value)

    return [hp.heappop(h) for i in range(len(h))]
    

a = [1,2,3,2,1,2,3,4,5,6,7,6,5,4]
hp.heapify(a)   
print(a)
# print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))