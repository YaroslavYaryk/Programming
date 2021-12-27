class Linkedlist:

    def __init__(self):
        self.head = None
        self.size = 0

    class Node:

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
            # a = toDelete
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

    def push(self, el):
        self._stack.push_back(el) 
    
    def is_empty(self):
        if self._stack.size != 0:
            return False
        return True
    
    def template(self, funk, text):
        if not self.is_empty():
            return funk()
        else:
            raise ValueError(text)

    def pop(self):
        return self.template(self._stack.pop_back, "Stack is empty")

    def show(self):
        return self.template(self._stack.treverse, "Can't show empty stack")

elem = Stack()
elem.push(1)
elem.push(2)            
elem.push(3)

print(elem.pop())          
print(elem.pop())  
print(elem.is_empty())          
# print(elem.pop())
elem.show()
