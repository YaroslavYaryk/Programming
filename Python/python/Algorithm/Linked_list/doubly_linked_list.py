class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None


    def insert_before_item(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.insert_at_start(data)              
                return
            elif cur.data == key:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node    
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next 

    def insert_at_end(self, data):
        
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            if data %2 ==0:
                self.insert_before_item(data, 0)


    def traverse_list(self):
        if self.head is None:
            print("List has no element")
            return
        else:
            cur = self.head
            while cur is not None:
                print(cur.data , " ")
                cur = cur.next                                


new_linked_list = DoublyLinkedList()
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(2)
new_linked_list.insert_at_end(8)

new_linked_list.insert_at_end(49)
new_linked_list.insert_at_end(50)
new_linked_list.insert_at_end(48)

new_linked_list.traverse_list()



