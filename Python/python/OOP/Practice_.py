import math
from math import pi


class Table(object):

    __slots__ = ("_height")

    def __init__(self, height):
        self._height = height


class Rect_table(Table):

    __slots__ = ("_width", "_lenth")

    def __init__(self, width, lenth, height=5):
        super().__init__(height)
        self._width = width
        self._lenth = lenth

    def __str__(self):
        return f"Rect_table({self._width},{self._lenth}, {self._height})"

    def area(self):
        return f"The area of rect_table is {self._width * self._lenth}  height = {self._height}"


class Circ_table(Table):

    __slots__ = ("_radius")

    def __init__(self, radius, height=5):
        super().__init__(height)
        self._radius = radius

    def __str__(self):
        return f"Circ_table({self._radius}, {self._height})"

    def area(self):
        return f"The area of circ_table is {round(pi * self._radius**2 , 2)} height = {self._height}"


table = Rect_table(3, 4)
table2 = Rect_table(11, 21)
table3 = Circ_table(3)
table4 = Circ_table(11)
c = [table, table2, table3, table4]
for item in c:
    print(item.area())
print()


class Animal(object):

    __slots__ = ("_name")

    def __init__(self, name):
        self._name = name

    def say(self):
        raise NotImplementedError("should be called in subclass")


class Fox(Animal):

    def __init__(self, name):
        super().__init__(name)

    
    def say(self):
        return f"{self._name} said brrr"


class Bird(Animal):

    def __init__(self, name):
        super().__init__(name)

    def say(self):
        return f"{self._name} said cvirk"


class Cat(Animal):

    def __init__(self, name):
        super().__init__(name)

    def say(self):
        return f"{self._name} said myau"


class Dog(Animal):

    def __init__(self, name):
        super().__init__(name)

    def say(self):
        return f"{self._name} said Gaff"


fox = Fox("Alisa")
bird = Bird("Valia")
cat = Cat("Julia")
dog = Dog("Alisson")
c = [fox, bird, cat, dog]
for item in c:
    print(item.say())
