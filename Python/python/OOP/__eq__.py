class Point(object):

    __slots__ = ("x" , "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    """ first of all __eq__ compare two point as their id()"""

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == self.y
    """ if we try to change __eq__ method it'll compare as their value"""

    def __hash__(self):
        return hash((self.x, self.y))


""" you have to know if we use __eq__ method we can't use hash() as function to our exempliar, its gonna 
be like,IndentationError: unexpected indent. if we wanna use hash() as function we have to change method __hase__
like i've done below """
""" it's useful when we have to put our object as key to some dictionary 
as you know as key we can put only """


point1 = Point(11, 12)
point2 = Point(11, 12)
point3 = Point(123, 234)
print(point1 == point2)
print(hash(point1))
