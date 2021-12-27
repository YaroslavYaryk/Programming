import weakref

a = {1,2,3}
wref = weakref.ref(a)
# print(wref)
# print(wref())

a = {1,2,3,4,5}
# print(wref())

class Cheese():

    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return str(self.kind)


stock = weakref.WeakValueDictionary()
values = [Cheese("first"), Cheese("second"), Cheese("third")]

for value in values:
    stock[value.kind] = value

print(sorted(stock.keys()))

del values
print(sorted(stock.keys()))

del value
print(sorted(stock.keys()))
