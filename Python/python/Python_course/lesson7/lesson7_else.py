import copy

class Counter(object):

    def __init__(self):
        self.lister = [1,2,3,4,5]
        self.num = 15


obj = Counter()
print(obj.lister)      
print(obj.num)
obj_copy = copy.copy(obj)  #when we use copy.copy() we just copy the object to another one
# if we change this obj_copy the original object will change as well
obj_copy.lister.append([1,2,3])     
print(obj_copy.lister)
print(obj.lister)  
obj2 = Counter()    
obj_copy2 = copy.deepcopy(obj2) # when we use copy.deepcopy() and if we wanna change the copy object then
# the original one doesnt change
obj_copy2.lister.append([1,2,3])
print(obj_copy2.lister)
print(obj2.lister)