def check_sorted(a:list, asserding = True):
    s = 2*int(asserding) -1
    flag = True
    for i in range(0, len(a) - 1):
        if a[i] > a[i+1]:
            flag = False
            break
    return flag

print(check_sorted([1,2,3,4,5,7,9]))        