
a = int(input())

def funk(n):
    d = {}
    counter = 0
    warning = 0
    for _ in range(n):
        b = input()
        if b not in d:
            d[b] = 1
        else:
            d[b] += 1
        counter +=1     
        
        if d[b] > 1 and (d[b] - 1 > counter - d[b]):
            warning +=1   
    return warning

print(funk(a))

                