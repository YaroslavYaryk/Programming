import numpy as np

class Stack(object):

    def __init__(self):
        self._stack = np.array([])
        self._size = 0
        self.storage = 0

    def push(self, el):
        self._stack = np.append(self._stack, el)
        self._size +=1

        if  1 <= self._size <=6:
            self.storage += el 

    def get_average(self):
        if  0 <= self._size < 6:
            raise ValueError("cant calculate average for < 6 elements")   
        else:
            return self.storage/6    

    def pop(self):
        self._size -=1
        a = self._stack[-1]
        self._stack = np.delete(self._stack, self._size)
        return a


    def is_empty(self):
        if len(self._stack) !=0:
            return False
        return True

    
elem = Stack()
for el in range(1,20):
    elem.push(el)



print(f"average value of 1-6 elem is - {elem.get_average()}")

