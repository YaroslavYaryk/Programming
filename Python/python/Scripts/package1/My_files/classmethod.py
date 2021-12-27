class Square:

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return f"Square({self.side_a} {self.side_b})"


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle({self.radius})"

    @classmethod
    def get_smth(cls, other):
        radius = ((other.side_a**2)+(other.side_b**2))**0.5
        return cls(radius)


square = Square(3,4)
print(square)
circle1 = Circle(5)
print(circle1)
circle2 = Circle.get_smth(square)
print(circle2)
