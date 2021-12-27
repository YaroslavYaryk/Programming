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



    def push_back(self, element):

        if not self.head:
            self.head = self.Node(element)

        else:
            node  = self.head
            while node.next:
                node = node.next

            node.next = self.Node(element) 
        self.size+=1    


    def insert(self,data, index, num = 1):

        if index == 0:
            self.push_front(data)

        previous = self.head
        for i in range(index-num):
            previous = previous.next

        new_Node = self.Node(data, previous.next)
        previous.next = new_Node
        self.size+=1


    def insert_before(self, data,index):

        self.insert(data,index, 2)

    
    def insert_after(self, data,index):

        self.insert(data,index, 0)


    def pop_front(self):

        node = self.head

        self.head = node.next

        del node

        self.size-=1 

    def pop_back(self):
        
        node = self.head
        for i in range(self.size-2):
            node = node.next

        toDelete = node.next
        node.next =toDelete.next
        del toDelete
        self.size-=1    




    def remove_id(self,index):

        if index ==0:
            self.pop_front()
        
        elif index > self.size-1:
            print( "Out of range")
            return

        else:
        
            previous = self.head
            
            for i in range(index-1):
                previous = previous.next

            toDelete = previous.next
            previous.next = toDelete.next
            del toDelete
            self.size-=1    

    def treverse(self):

        node = self.head

        while node.next:
            print(node.element)
            node = node.next
        print(node.element)  


    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev          


    def __del__(self):
        while self.size:
            self.pop_front()


link = Linkedlist()
link.push_back(2)
link.push_back(12)

link.push_back(4)
link.remove_id(0)


(link.treverse())
link.reverse()
(link.treverse())

# link.pop_back()
# link.pop_front()

# link.append(5)
# link.append(6)
# link.append(7)
# link.insert(3,2)
# link.insert_before(7,2)
# link.insert_after(9,3)


# (link.out())
