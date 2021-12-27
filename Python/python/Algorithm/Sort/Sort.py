class Bubble_sort(object):

    @staticmethod
    def isList(value):
        return isinstance(value, list)

    def __init__(self, list):
        if Bubble_sort.isList(list):
            self.list = list

    def __call__(self):

        for i in range(len(self.list)-1):
            for j in range(len(self.list)-1-i):
                if self.list[j] > self.list[j+1]:
                    self.list[j+1], self.list[j] = self.list[j], self.list[j+1]
        return self.list

a = [2,1,4,3,7,5,8,9,0]
bubble = Bubble_sort(a)
print(bubble())


class Assertion(object):

    @staticmethod
    def isList(value):
        return isinstance(value, list)

    def __init__(self, list):
        if Assertion.isList(list):
            self.list = list

    def __call__(self):

        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i - 1 
            while j >=0 and key < self.list[j] :
                self.list[j+1] = self.list[j]
                j -= 1
            self.list[j+1] = key
        return self.list     

a = [2,1,4,3,7,5,8,9,0]
bubble = Assertion(a)
print(bubble()) 
