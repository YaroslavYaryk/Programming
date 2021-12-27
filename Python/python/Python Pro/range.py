def square(items):
    for item in items:
        yield item * item

a = square([1,2,3])

print(next(a)) 
print(next(a))      
print(next(a))      


