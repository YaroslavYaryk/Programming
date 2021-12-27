class Linkedlist:

    def __init__(self):
        self.head = None
        self.size = 0

    class Node:

        def __init__(self, element, next = None):
            self.element = element
            self.next = next

    def push_front(self, data):

        self.head = self.Node(data,self.head)
        self.size += 1    


    def pop_front(self):

        node = self.head

        self.head = node.next
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


    

class Queue(object):

    def __init__(self):
        self._queue = Linkedlist() 

    def is_empty(self):
        return self._queue.size == 0

    def add(self, x):
        self._queue.push_front(x)
        
    def template(self, funk, text):
        if not self.is_empty():
            return funk()
        else:
            raise ValueError(text)


    def remove(self):
        return self.template(self._queue.pop_front, "Queue is empty")
            


    def show(self):
        return self.template(self._queue.treverse, "Can't show empty queue")
            


obj = Queue()
obj.add(1)        
obj.add(2)        
obj.add(3)
print(obj.remove())
print(obj.remove())        
print(obj.remove())
print(obj.is_empty())
# obj.show()
