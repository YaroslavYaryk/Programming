class Linkedlist:

    __slots__ = ("head", "size")

    def __init__(self):
        self.head = None
        self.size = 0

    class Node:

        __slots__ = ("element", "next")

        def __init__(self, element, next = None):
            self.element = element
            self.next = next

    def push_back(self, element):

        if not self.head:
            self.head = self.Node(element)

        else:
            node  = self.head
            while node.next:
                node = node.next

            node.next = self.Node(element) 
        self.size+=1    


    def pop_back(self):
        
        node = self.head
        for i in range(self.size-2):
            node = node.next
        if self.size !=1:
            toDelete = node.next
            node.next =toDelete.next
            a = toDelete
            del toDelete
            
        else:
            a = node
            del node
                 
        self.size-=1        
        return a.element

    def treverse(self):

        node = self.head

        while node.next:
            print(node.element)
            node = node.next
        print(node.element)  


class Stack(object):

    def __init__(self):
        self._stack = Linkedlist()
        self.storage = 0

    def push(self, el):
        self._stack.push_back(el) 
        if  1 <= self._stack.size <=6:
            self.storage += el

    def get_average(self):
        if  0 <= self._stack.size < 6:
            raise ValueError("cant calculate average for < 6 elements")   
        else:
            return self.storage/6         
    
    def is_empty(self):
        if self._stack.size != 0:
            return False
        return True
    
    def return_teplate_function(self, funk, text):
        if not self.is_empty():
            return funk()
        else:
            raise ValueError(text)

    def pop(self):
        return self.return_teplate_function(self._stack.pop_back, "Stack is empty")

    def show(self):
        return self.return_teplate_function(self._stack.treverse, "Can't show empty stack")



elem = Stack()
for el in range(1,20):
    elem.push(el)

print(f"average value of 1-6 elem is - {elem.get_average()}")