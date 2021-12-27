class NonNegative(object):
    def __set_name__(self,owner,name):
        self.name = name
    def __get__(self,instance,owner):    
        return instance.__dict__[self.name]

    def __set__(self,instance,value):
        if value < 0:
            raise ValueError("can't be negative")
        else:
            instance.__dict__[self.name] = value


class Store(object):
    price = NonNegative()

    def __init__(self, price):
        self.price = price

    def getter(self):
        return self.price


owner = Store(11)       
print(owner.getter())             



class Store2(object):

    def __init__(self, price):
        self.price = price
    @property
    def prrr(self):
        return self.price

    @prrr.setter
    def prrr(self, value):
        if value < 0:
            raise ValueError("can't be negative")
        else:
            self.price = value


owner = Store2(11)       
print(owner.prrr)
owner.prrr = 22
print(owner.prrr)


