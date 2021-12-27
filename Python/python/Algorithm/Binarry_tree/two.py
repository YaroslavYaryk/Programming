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
            print(f"\nValue({value}) already in tree\n")    


    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left)
            print(str(cur_node.value), end= " ")
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
            return f"\n\n{value}  is in tree\n"
        elif value < cur_node.value and cur_node.left is not None:
            return self._search(value, cur_node.left)
        elif value > cur_node.value and cur_node.right is not None:
            return self._search(value, cur_node.right)
        else:
            return f"\nthere is no {value} in tree\n"



    def find_max(self):
        if self.root is not None:
            return self._find_max(self.root)
        else:
            return False   

    def _find_max(self,cur_node):
        if cur_node.right is None:
            return cur_node.value        
        return self._find_max(cur_node.right)    


    def find_min(self):
        if self.root is not None:
            return self._find_min(self.root) 
        return False

    def _find_min(self,cur_node):
        if cur_node.left is not None:
            return self._find_min(cur_node.left)
        else:
            return cur_node.value      


    def delete_Node(self, key):
        if not self.root: 
            return root
        return self._delete(key, self.root)


    def _delete(self, value, cur_node):  
        if not cur_node:
            return cur_node
        if cur_node.value > value: 
            cur_node.left = self._delete(value, cur_node.left)
        elif cur_node.value < value: 
            cur_node.right = self._delete(value, cur_node.right)
        else: 

            if not cur_node.right:
                return cur_node.left
            if not cur_node.left:
                return cur_node.right

            temp_val = cur_node.right
            mini_val = temp_val.value

            while temp_val.left:

                temp_val = temp_val.left
                mini_val = temp_val.value

            cur_node.right = self._delete(value, cur_node.right)
        
        return cur_node




tree = Tree()
tree.insert(5)
tree.insert(10)
tree.insert(4)
tree.insert(2)
tree.insert(7)
tree.insert(10)
tree.print_tree()  

tree.delete_Node(2)


print(tree.search(10))
tree.print_tree()            
