class City(object):

    __slots__ = ("name")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name.title()

    def __bool__(self):
        c = ["a", "o", "u", "e", "i"]
        for i in c:
            if self.name[-1] == i:
                return False
            return True
            

p1 = City('new york')
print(p1)  # печатает "New York"
print(bool(p1))  # печатает "True"
p2 = City('SaN frANCISco')
print(p2)  # печатает "San Francisco"
print(p2 == True)  # печатает "False"            

class Quadrilateral(object):

    __slots__ = ("width", "height")

    def __init__(self, *args):
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
        else:
            self.width = args[0]
            self.height = args[1]

    def __str__(self):
        if self.width == self.height:
            return f"cube size <{self.width}>x<{self.height}>"
        return  f"Quadrilateral size <{self.width}>x<{self.height}>"

    def __bool__(self):
        return self.width == self.height               


q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False