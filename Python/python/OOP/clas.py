class Tryk:

    __slots__ = ("side_x")

    def __init__(self, side):
        self.side_x = side

    def __str__(self):
        return f"Tryk({self.side_x})"


class Circle:

    __slots__ = ("radius")

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle({self.radius})"

    @classmethod
    def kolo(cls, circle):
        radius = round(circle.side_x/(3**0.5), 2)
        return cls(radius)


tryk = Tryk(10)
print(tryk)
first = Circle(5)
print(first)
second = Circle.kolo(tryk)
print(second)
