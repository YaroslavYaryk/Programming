import random

class Sort(object):

    def __init__(self, A:list):
         self.A = A

    def insert_sort(self):
        n = len(self.A)
        for i in range(n):
            j = i
            while j>0 and self.A[j-1] > self.A[j]:
                self.A[j-1], self.A[j] = self.A[j], self.A[j-1]
                j-=1
        return self.A


    def choice_sort(self):
        n = len(self.A)
        for pos in range(n-1):
            for k in range(pos+1, n):
                if self.A[k] < self.A[pos]:
                    self.A[k], self.A[pos] = self.A[pos] , self.A[k]    
        return self.A


    def buble_sort(self):
        n = len(self.A)
        for i in range(1, n):
            for j in range(n-i):
                if self.A[j] > self.A[j+1]:
                    self.A[j], self.A[j+1] = self.A[j+1], self.A[j]    
        return self.A


    def count_sorted(self):
        max_el = max(self.A)
        cnt = [0] * (max_el + 1)

        for i in range(len(self.A)):
            cnt[self.A[i]] += 1

        pos = 0
        for num in range(len(cnt)):
            for i in range(cnt[num]):
                self.A[pos] = num
                pos += 1    
        return self.A

    @staticmethod
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


obj = Sort(list(random.sample(range(20),10))) 
print(obj.QuickSort(random.sample(range(20),10)))      

