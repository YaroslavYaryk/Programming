from Examples_deskriptors import Check_int_float

class Store(object):
    hello  = Check_int_float()

    def __init__(self, price):
        self.hello = price

    def getter(self):
        return self.hello

van = Store("sr")
