from math import factorial  

m, k = map(int, (input().split()))

n = 2

while factorial(n) % m**k != 0:
    n+=1

print(n)    

