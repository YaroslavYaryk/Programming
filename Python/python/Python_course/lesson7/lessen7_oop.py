import random
from decimal import Decimal
from fractions import Fraction 
import datetime
class Mine():

    def __init__(self):
        a = 10

    def gwt_rand(self):
        return random.sample(range(100), 5)    


# obj = Mine()
# print(obj.gwt_rand())        

a = Decimal("0.1") + Decimal("0.2") # Decimal is like a float but when we add two 
# floats like (0.1 + 0.2) we get 0.300000000004
# but when we use Decimal we get better one , like we used round()
print(Fraction(2,3)) # when we dilymo one number to another and if they are like 
# 1/3 we get 0.333333333333  but when we use Fraction(1,3) we get (1/3) we dont lose the occurate
print(2 + Fraction(1,3) + Fraction(2,3))

print(datetime.datetime.now())