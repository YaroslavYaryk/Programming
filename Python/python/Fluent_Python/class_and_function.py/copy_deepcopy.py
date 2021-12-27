import copy




class Buss(object):

    def __init__(self, objects = None):

        if objects is None:
            self.storage = []
        else:
            self.storage = list(objects)    


    def push(self, elem):
        self.storage.append(elem)


    def pop(self, elem):

        self.storage.remove(elem)

a = Buss(["Bill", "Cody", "Shell"])
b = copy.copy(a)
c = copy.deepcopy(a)

print(id(a), "  ", id(b), "  ", id(c))

a.push("John")

print(id(a.storage), "  ", id(b.storage), "  ", id(c.storage))
