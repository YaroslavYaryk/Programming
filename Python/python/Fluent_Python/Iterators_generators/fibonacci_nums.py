def fibonacci(num):
    
    first, second = 0,1
    for i in range(num):
        first, second = second, first + second
        yield first
        

k = fibonacci(100)
for i in k:
    print(i)        