def binarry(lister, start, end, key):

    mid  = (start + end)//2

    if lister[mid] ==key:
        return mid
    elif lister[mid] > key:
        return binarry(lister,start, mid, key) 
    else:
        return binarry(lister, mid, end, key)       

# a = [1,2,3,4,5,6,7,8,76]
# print(binarry(a, 0 , len(a) ,5))    


def just_binarry(lister, start, end, key):

    mid = (start + end)//2

    while start  <  end:
        if lister[mid] == key:
            return mid
        elif lister[mid] > key:
            right = mid
        else:
            left = mid        
    
a = [1,2,3,4,5,6,7,8,76]
print(just_binarry(a,0,len(a),5))