class Vector(object):
    
    __slots__ = ("values", "coard_x", "coard_y", "coard_z")

    def __init__(self, *args):
        self.values = list(args)
        self.coard_x = int(format(self.values[0]))
        self.coard_y = int(format(self.values[1]))
        self.coard_z = int(format(self.values[2]))

    def __str__(self):
        if self.coard_x != 0 and self.coard_y != 0 and self.coard_z != 0:
            return f"Vector <{self.coard_x}>, <{self.coard_y}>, <{self.coard_z}>"
        else:
            return f"empty vector"      


    

    def __add__(self, other):

        if isinstance(other, int):
            return Vector(self.coard_x + other, self.coard_y + other, self.coard_z + other)
        elif isinstance(other, Vector):
            if len(self.values) != len(other.values):
                return "can't add two different lens vektors"
            return Vector(self.coard_x + other.coard_x, self.coard_y + other.coard_y, self.coard_z + other.coard_z)
        elif isinstance(other, str):
            return f"cant add vector to <{other}>"
            
        
        

    def __mul__(self, other):

        if isinstance(other, int):
            return Vector(self.coard_x * other, self.coard_y * other, self.coard_z * other)
        elif isinstance(other, Vector):
            if len(self) != len(other):
                return "can't add two different lens vektors"
            return Vector(self.coard_x * other.coard_x, self.coard_y * other.coard_y, self.coard_z * other.coard_z)
        
        else:
            return f"cant add vector to <{other}>"
                    


v1 = Vector(0,0,0)
print(v1) # печатает "Вектор(1, 2, 3)"
v2 = Vector(3,4,5)
print(v2) # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3) # печатает "Вектор(4, 6, 8)"s
v5 = v2 * 2
print(v5) # печатает "Вектор(2, 4, 6)"
print(v5 + 'hi') # печатает "Вектор нельзя сложить с hi"
v6 = Vector(1,2,3,4)
print(v6 + v2)