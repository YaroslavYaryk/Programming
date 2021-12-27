
class DDict(object):

    def __init__(self):
        self.storage = {}

    def __repr__(self):
        return f"{self.storage}"

    def __missing__(self, key):
        if key not in self.storage:
            return "sorry but i can't find this element"
        return self.storage[key]    

    def __setitem__(self, key, value):

        if hash(key):
            self.storage[key] = value
        else:
            raise hashError("unheshable type")

    def __getitem__(self, key):
        if key in self.storage:
            return self.storage[key]      
        return DDict.__missing__(self, key)          



a = DDict()
# a[12] = "hello"
# a[22] = "world"
# a[33] = "and"

# print(a[22])

d = {}
d.update({2: 123})
d.update({3: 124})
d.update({4: 125})
print(d.setdefault(5,234))
print(d)