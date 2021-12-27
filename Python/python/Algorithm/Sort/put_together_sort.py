def merge_sort(A):

    if len(A) <=1:
        return

    midle = len(A)//2
    L = A[:midle] 
    R = A[midle:]
    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1


    while i < len(L):
        A[k] = L[i] 
        i+=1
        k+=1

    while j < len(R):
        A[k] = R[j]
        j+=1
        k+=1
    

    return A


a = [1,3,5,7,9]
b = [2,4,6,8]
# print(merge(a,b))
print(merge_sort([12, 11, 13, 5, 6, 7]))        

