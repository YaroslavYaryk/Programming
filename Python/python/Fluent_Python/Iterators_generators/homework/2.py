class Reversed:
    
    def __init__(self, iterable):
        self._elements = iterable
        self._index = 0
    
    def __iter__(self):
        for i in range(len(self._elements), 0, -1):
            yield i
    
    
             
ind = Reversed([1,2,3,4,5,6,7,8,9])
for i in ind:
    print(i)             
             