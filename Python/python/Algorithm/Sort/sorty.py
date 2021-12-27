class Select_sort(object):

    __slots__ = ("arr")

    def __init__(self, lister):
        self.arr = lister

    def __str__(self):
        return f"List - {self.arr}"    


    def find_smallest(self,arr):

        smallest = self.arr[0]
        index = 0
        for i in range(1,len(self.arr)):
            if self.arr[i] < smallest:
                smallest = self.arr[i]
                index = i
        return index    


    
    def find_biggest(self,arr):
        biggest = self.arr[0]
        index = 0
        for i in range(1,len(self.arr)):
            if self.arr[i] > biggest:
                biggest = self.arr[i]
                index = i
        return index     

    def Operation(self,funk):
        new_one = []

        for i in range(len(self.arr)):
            oper = funk(self.arr)
            new_one.append(self.arr.pop(oper))
        return new_one      


    def __call__(self,word):

        if word == "down":
            return self.Operation(self.find_biggest)
        
        elif word == "up":
            return self.Operation(self.find_smallest)

            

lister = [5, 3, 6, 2, 10]
a = Select_sort(lister)
print(a)
# print(a("up"))
print(a("down"))



