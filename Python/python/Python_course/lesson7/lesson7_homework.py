import math
class Simple(object):

    def __init__(self, num):
        self._num = num

    @staticmethod
    def is_prime(n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def geter(self):
        for numb in range(2,self._num):
            if Simple.is_prime(numb):
                print(numb, end = " ")
                 

# some = Simple(17)
# # print(some.is_prime(17))
# # print(some._num)
# some.geter()