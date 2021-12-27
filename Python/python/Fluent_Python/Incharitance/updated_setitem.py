from collections import UserDict
from inspect import k

class Simple_dict(dict): # when we incharit from just Dict 
# this class ignore everything what we overloded 
# #so we should inheret from "collection" UserDict or other classes in this collection    

    def __setitem__(self, key, value):

        super().__setitem__(key, value*2)

    def __getitem__(self, key):
        return 42    


kk = Simple_dict(a = "foo")

# print(kk["a"])


d = {}
d.update(kk)
# print(d, "\n\n")          


class Simple_dict(UserDict):  

    def __setitem__(self, key, value):

        super().__setitem__(key, value)

    def __getitem__(self, key):
        return 42     

    def __len__(self):
        return super().__len__()

    def __contains__(self, key):
        return super().__contains__(key)

    def __eq__(self, value):
        return super().__eq__(value) 

    def __hash__(self):
        return super().__hash__()           


kk = Simple_dict(a = "foo")

# print(kk["a"])

d = {}
d.update(kk)
# print(d)           

"""42   -> Dict
{'a': 'foo'} 


42    -> UserDict
{'a': 42}
"""


e = Simple_dict(a = 100)
c = Simple_dict(b = 200)

print(e == c)
