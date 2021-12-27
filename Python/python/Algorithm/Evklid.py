def gcd(a,b):
    
    return a if b==0 else gcd(b, a%b)

print(gcd(127, 254))

def gcd2(a,b):

    if a == b:
        return a
    elif a>b:
        return gcd2(a-b,b) 
    else:
        return gcd2(a,b-a)       


print(gcd2(123,273))        