class Operations(object):

    def __init__(self, one, two):
        self.a = one
        self.b = two

    def sered(self):
        return (self.a + self.b)/2 

    def __which_bigger(self):
        self.a < self.b

    def prom(self):
        a = 0
        if self.a < self.b:
            for i in range(self.a, self.b+1):
                a+=i

            return a/(self.b - self.a +1) 
        else:
            for i in range(self.b, self.a+1):
                a+=i


            return a/(self.a - self.b + 1)             

oper = Operations(11,23)
print(oper.prom())            