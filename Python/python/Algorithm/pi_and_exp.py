from math import pi, e
def Pi(n):

    res = 0.0
    for i in range( n+1):
        res += (4 * (-1)**i) / (2*i+1)

    return res
    
print(pi)
print(Pi(10000))
print()

def fact(n):
    storage = 1
    for i in range(2,n+1):
        storage *= i
    return storage

def Exp(n):
    res = 0.0
    for i in range(n+1): 
        res += (1)**i / (fact(i))
    return res

print(e)
print(Exp(1000))
