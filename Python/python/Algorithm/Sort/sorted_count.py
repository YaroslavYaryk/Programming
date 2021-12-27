import random
arr = [1,2,3,2,1,2,3,4,5,6,5,4,3,4,5,6,5]

def sort_count(mas:list):
    a = [0] * (max(mas)+1)
    for num  in range(len(mas)):
        a[mas[num]] +=1
    

    pos = 0
    for num1 in range(len(a)):
        for j in range(a[num1]):
            mas[pos] = num1
            pos+=1
    return mas

# print(sort_count(arr))            

def QuickSort(A):
        if len(A) <= 1:
            return A
        else:
            q = random.choice(A)
            L = []
            M = []
            R = []
            for elem in A:
                if elem < q:
                    L.append(elem) 
                elif elem > q: 
                    R.append(elem) 
                else: 
                    M.append(elem)
            return QuickSort(L) + M + QuickSort(R)

print(QuickSort(arr))            