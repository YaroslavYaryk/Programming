class List():
    
    class Node():
        def __init__(self, value, next = None):
            self.value = value
            self.next = next
    
    
    def __init__(self, iterable = None):
        self._head = None
        self._tail = None
        self.lenth = 0
    
        if iterable is not None:
            self.extend(iterable)    
    
    def __iter__(self):
        node = self._head  
        while node is not None:
            yield node.value
            node = node.next 
    
    def append(self, value):
        node = List.Node(value)
        if self.lenth == 0:
            self._head = self._tail = node
        
        else:
            self._tail.next = node
            self._tail = node
        self.lenth += 1    
            
    def __len__(self):
        return self.lenth        
            
    def extend(self,iteration):
        for i in iteration:
            self.append(i)
            
    def __getitem__(self, index):
        if index < 0:
            index +=len(self)
        
        if not 0 <= index < len(self):
            raise IndexError("out of range")    
        
        node = self._head
        for i in range(index):
            node = node.next
        return node.value
    

obj = List(range(100))
for i in obj:
    if i %2 == 0: 
        print(i)           
                                
            
        
                    