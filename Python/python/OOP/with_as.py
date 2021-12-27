# import time

# class Timer(object):
    
#     __slots__ = ("_variable")

#     def __enter__(self):
#         self._variable = time.time()

#     def __exit__(self,type, value, traceback):
#         print ( time.time() - self._variable)


# with Timer():
#     for i in range(10000):
#         print(i)           


class Aditional(object):

    def __init__(self,v):
        self._v = v

    def __enter__(self):
        self.__t = self._v
        return self.__t

    def __exit__(self, exc_cls,*args):
        if exc_cls is None:
            self._v = self.__t


v1 = [1,2,3]
v2 = [1,2,3]
with Aditional(v1)  as dv:
    for i in range(len(dv)):
        dv[i] += v2[i]

print(v1)                    