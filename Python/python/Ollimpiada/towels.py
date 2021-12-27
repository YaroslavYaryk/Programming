def is_towel(n):
    if n == 1:
        return True
    for i in range(2, int(n**0.5) +1):
        for j in range(i, int(n**0.5) +1):
            if i**j == n:
                return True
    return False             
            
n = int(input())
counter = 0
for i in range(1,n+1):
    if (is_towel(i)):
        counter +=1   
print(counter)    
