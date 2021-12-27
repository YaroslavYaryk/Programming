import timeit

def f1():
    for n in range(100):
        pass

def f2():
    n=0
    while n<100:
        n+=1

if __name__ == "__main__":
    import timeit    
    print (timeit.timeit(f1, number=100000))
    print (timeit.timeit(f2, number=100000))