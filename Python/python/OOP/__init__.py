class Father(object):
    
    __slots__ = ("_side_a")

    def __init__(self, side_a):
        self._side_a = side_a

class Triangle(Father):
    
    __slots__ = ("_side_b", "_side_c")

    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a)
        self._side_b = side_b
        self._side_c = side_c

    def __str__(self):
        return f"Triangle ({self._side_a} {self._side_b} {self._side_c})"    

    def get_area(self):
        p = (self._side_a + self._side_b + self._side_c)/2
        S = (p*(p-self._side_a)*(p-self._side_b)*(p-self._side_c))**0.5
        return round(S) 

class Square(Father):

    def __init__(self, side_a):
        super().__init__(side_a)

    def __str__(self):
        return f"Square ({self._side_a})"

    def get_area(self):
        S  = self._side_a ** 2
        return S 

triangle1 = Triangle(3,4,5)
triangle2 = Triangle(10,20,28)
square1 = Square(10)
square = Square(20)

list= [triangle1,triangle2, square1, square ]
for figure in list:
    print(figure, "=" ,figure.get_area())











