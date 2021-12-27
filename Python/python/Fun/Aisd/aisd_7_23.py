class Node:
    
    def __init__(self, value, sex = None):

        self.left = None
        self.right = None
        self.value = value
        self.sex = sex

class Tree:

    def __init__(self):
        self.root = None
        self.flag = False

    def insert(self, data,sex):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root,self.flag)

    def _insert(self, value, cur_node,flag):
        if self.flag is True:
            if cur_node.left is None:
                cur_node.left = Node(value)
                self.flag = not self.flag
            else:
                self._insert(value, cur_node.left, not self.flag)
        else:
            if cur_node.right is None:
                cur_node.right = Node(value)     
                self.flag = not self.flag
            else:
                self._insert(value, cur_node.right,not self.flag)    

    # Print the tree

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root.left)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)   
    
    # def get_grand(self):
    #     if self.root.left:
    #         print("Прабабуся ", self.root.left.data)

    # def print_granny(self):
    #     head = self.root
    #     if self.root.left:
    #         self.cont_print(head)

    # def cont_print(self, cur_node):
    #     head = cur_node.left
        
    #     if self.root.left:
    #         self.get_grand()
    #     if self.root.right:
    #         self.get_grand()



root = Tree()
root.insert("me", "m")
root.insert("Grand_Pasha","m")
root.insert("Dad", "m")
root.insert("Mom", "f")
root.insert("Grand_Olia", "f")
root.insert("Grand_Roma","m")
root.insert("Grand_Masha", "f")
root.insert("Grandgranddad1","m")
root.insert("Grandgrandmom1", "f")
root.insert("Grandgranddad2","m")
root.insert("Grandgrandmom2", "f")
root.insert("Grandgranddad3","m")
root.insert("Grandgrandmom3", "f")
root.insert("Grandgranddad4","m")
root.insert("Grandgrandmom4", "f")
root.print_tree()