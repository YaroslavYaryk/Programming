class Parents:
    def __init__(self, a):
        self._a = a


class Triangle(Parents):
    def __init__(self, a, b=2, c=3):
        super().__init__(a)
        self._b = b
        self._c = c

    def __str__(self):
        return f"Triangle ({self._a} {self._b} {self._c})"

    def get_area(self):
        p = (self._a + self._b + self._c) / 2
        S = ((p - self._a) * (p - self._b) * (p - self._c)) ** 0.5
        return round(S)


class Square(Parents):
    def __init__(self, a):
        super(Square, self).__init__(a)

    def __str__(self):
        return f"Square ({self._a})"

    def get_area(self):
        S = self._a ** 2
        return S


class Rectangle(Parents):
    def __init__(self, a, b):
        super().__init__(a)
        self._b = b

    def __str__(self):
        return f"Rectangle ({self._a} {self._b})"

    def get_area(self):
        S = self._a * self._b
        return S


triangle1 = Triangle(10, 20, 25)
triangle2 = Triangle(11, 22, 28)
square1 = Square(10)
square2 = Square(20)
rectangle1 = Rectangle(11, 22)
rectangle2 = Rectangle(10, 20)

list = [triangle1, triangle2, square1, square2, rectangle1, rectangle2]

for figure in list:
    print(figure, "=", figure.get_area())
