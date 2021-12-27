class Kvadr:

    __slots__ = ("coardx", "coardy")

    def __init__(self, coardx, coardy):
        self.coardx = coardx
        self.coardy = coardy

    def __str__(self):
        return f"Kvadr({self.coardx}, {self.coardy})"


class Circle:

    __slots__ = ("__circle")

    def __init__(self, circle):
        self.__circle = circle

    def __str__(self):
        return f"Circle({self.__circle})"

    @classmethod
    def printa(cls, value):
        result = value.coardx + value.coardy
        return cls(result)


coard = Kvadr(11, 5)
print(coard)
first = Circle(10)
print(first)
second = Circle.printa(coard)
print(second)