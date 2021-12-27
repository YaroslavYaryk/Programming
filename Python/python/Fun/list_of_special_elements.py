def show_elem(n:int):
    a = [0]*(n+1)
    x = 0
    y = 1
    a[0] = 1
    a[1] = 100
    while not a[n-1]:
        a[x+2] = a[x] + 1
        a[y+2] = a[y] * 2

        x+=2
        y+=2 
    return a[n-1]

print(show_elem(101))

