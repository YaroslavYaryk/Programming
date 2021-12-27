class Work_ticket(object):

    __slots__ = ("_name", "_age", "_balance")

    def __init__(self, name, age, balance):
        self._name = name
        self._age = age
        self._balance = balance

    def __repr__(self):
        return f"Work_ticket({self._name}, {self._age}, {self._balance})"

    def __add__(self, other):
        if isinstance(other, int):
            return Work_ticket(self._name, self._age + other, self._balance + other)
        elif isinstance(other, Work_ticket):
            return Work_ticket(self._name, self._age + other._age, self._balance + other._balance)
        elif isinstance(other, str):
            return Work_ticket(self._name, str(self._age) + other, str(self._balance) + other) 
        else:
            raise NotImplementedError

    def __mul__(self, other): 
        if isinstance(other, int):
            return Work_ticket(self._name, self._age * other, self._balance * other)
        elif isinstance(other, Work_ticket):
            return Work_ticket(self._name, self._age * other._age, self._balance * other._balance) 
        else:
            raise NotImplementedError

    def __truediv__(self, other):    
        if isinstance(other, int):
            return Work_ticket(self._name, round(self._age / other, 2), round(self._balance / other, 2))
        elif isinstance(other, Work_ticket):
            return Work_ticket(self._name, round(self._age / other._age, 2), round(self._balance / other._balance, 2)) 
        else:
            raise NotImplementedError       
 
    def __sub__(self, other):
        if isinstance(other, int):
            return Work_ticket(self._name, self._age - other, self._balance - other)
        elif isinstance(other, Work_ticket):
            return Work_ticket(self._name, self._age - other._age, self._balance - other._balance) 
        else:
            raise NotImplementedError

    def __pow__(self, other):
        if isinstance(other, int):
            return Work_ticket(self._name, self._age ** other, self._balance ** other)
        elif isinstance(other, Work_ticket):
            return Work_ticket(self._name, self._age ** other._age, self._balance * other._balance) 
        else:
            raise NotImplementedError    

imployee1 = Work_ticket("Yaroslav", 17, 100)
imployee2 = Work_ticket("Olha", 15, 500)
print(imployee1 + imployee2)
print(imployee1 - imployee2)
print(imployee1 * imployee2)
print(imployee1 / imployee2)
print(imployee1 ** imployee2)