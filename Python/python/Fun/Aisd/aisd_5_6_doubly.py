import time
from random import sample, choice

a = sample(range(1,11), 10)
b = sample(range(1,10001), 10000)

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

storage = 0
a = list(sample(range(101), 100))
for i in range(100):
    chosen_elem = choice(a)
    if chosen_elem == 0:
        storage += 1
        continue
    else:
        new_linked_list.insert_at_end(chosen_elem)

for elem in range(storage):
    new_linked_list.insert_at_end(0)

new_linked_list.traverse_list()    