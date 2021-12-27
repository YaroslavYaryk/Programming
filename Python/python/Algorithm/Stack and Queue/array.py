class Stack(object):

    def __init__(self):
        self._stack = []

    def push(self, el):
        self._stack.append(el) 

    def pop(self):
        return self._stack.pop()

    def clear(self):
        self._stack.clear()

    def is_empty(self):
        if len(self._stack) !=0:
            return False
        return True

    def __del__(self):
        Stack.clear(self)    

elem = Stack()
elem.push(1)
elem.push(2)            
elem.push(3)
print(elem.is_empty())  
print(elem.pop())          
print(elem.pop())          
print(elem.pop())
print(elem.is_empty())  
del elem           
print()

class Queue(object):

    def __init__(self):
        self.queue = []
        self.top = 0 

    def is_empty(self):
        return len(self.queue) == 0

    def add(self, x):
        self.queue.append(x)
        

    def remove(self):
        if not self.is_empty():
            self.top += 1
            return self.queue[self.top - 1]
    
    def clear(self):
        self.queue.clear()

    def show(self):
        return self.queue 


obj = Queue()
print(obj.is_empty())
obj.add(1)        
obj.add(2)        
obj.add(3)
print(obj.remove())
print(obj.remove())        
print(obj.remove())      
obj.clear()  
print(obj.is_empty())
print(obj.show())
