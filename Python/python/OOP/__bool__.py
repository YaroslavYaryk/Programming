class Point(object):

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __len__(self):
        print("call __len__")
        return abs(self.x - self.y)

# """if we dont have __bool__ method we're gonna use __len__ and get: 
# call __len__
# True
# """
    def __bool__(self):
        print("call __bool__")
        if self.x==0 and self.y ==0:
            return False
        return True        

""" if we have __bool__ to bool(someth) we'll get this one:
call __bool__
True
"""

point1 = Point(11,22)
print(bool(point1))




