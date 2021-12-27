class Node:

    __slots__ = ("left", "right", "value")

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

class Tree:

    __slots__ = ("root", "storage", "a")

    def __init__(self):
        self.root = None 
        self.storage = {}


    def add_to_dict(self, elem): #add specicfic element to dict in order to count levels
        if elem  in self.storage:
            self.storage[elem] +=1
        else:
            self.storage[elem] = 1


    def insert(self, value): #add element to tree
        i = 1
        self.add_to_dict(1) #add to dict

        if self.root is None:
            self.root = Node(value) #if root is None - create a new root
        else:
            self._insert(value, self.root, i) # else add it to level below

    def _insert(self, value, cur_node, i):
        i+=1
        if value < cur_node.value:  #if elem is lowwer than cur_elem send it to the left tree
            if cur_node.left is None:
                cur_node.left = Node(value) #if first left tree is None put this element into this place
            else:
                self._insert(value, cur_node.left, i) # else add it to level below 

        elif value > cur_node.value: #if elem is larger than cur_elem send it to the right tree
            if cur_node.right is None:
                cur_node.right = Node(value) #if first right tree is None put this element into this place    
            else:
                self._insert(value,cur_node.right, i) # else add it to level below

        self.add_to_dict(i)  #add level  to dict
                

    def height(self):
        if self.root is not None: #calculate height by going down 
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self,cur_node, cur_height):
        if cur_node is  None:
            return cur_height 
        else:
            left_height = self._height(cur_node.left, cur_height + 1 ) # going down by left tree
            right_height = self._height(cur_node.right, cur_height + 1) # going down by right tree
            return max(left_height, right_height) #get bigger one                  



    def get_nodes(self):
        for elem in range(1,len(self.storage)): #make a dict show correct integers
            self.storage[elem] -= self.storage[elem+1]

        return self.storage #return this dict


    def __getitem__(self,index): #overload the breckets "[]" to get the key from the dict
        self.a = self.get_nodes()
        try:
            return self.a[index] #if index is correct return value

        except KeyError: #if key out of range
            return 0 #return 0


tree = Tree()
tree.insert(5)
tree.insert(3)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(2)


height = tree.height() 
print(f"{tree[height]} - nodes on the bottom level")
