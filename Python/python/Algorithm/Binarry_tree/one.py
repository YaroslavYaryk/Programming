class Node:

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value

class Tree:

    def __init__(self):
        self.root = None #корень дерева        
    def insert(self, value):
        if self.root is None:
            self.root =Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value, cur_node.left)

        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)     
            else:
                self._insert(value,cur_node.right) 

        else:
            print(f"Value({value}) already in tree")    


    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value))
            self._print_tree(cur_node.right)                         


    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self,cur_node, cur_height):
        if cur_node is  None:
            return cur_height
        else:
            left_height = self._height(cur_node.left, cur_height+1 )
            right_height = self._height(cur_node.right, cur_height +1)
            return max(left_height, right_height)                 


    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return f"{value}  is in tree"
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return False




tree = Tree()
tree.insert(5)
tree.insert(10)
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.print_tree()            
print("heigh is:", tree.height())
print(tree.search(7))

