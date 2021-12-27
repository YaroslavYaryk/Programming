import datetime


start = datetime.datetime.now()
class Factorial(object):

    __slots__ = ("storage")

    def __init__(self):
        self.storage = {}

    def __call__(self, n):


        if n not in self.storage:
            if n == 0:
                self.storage[n] = 1
            else:
                self.storage[n] = n * self.__call__(n-1)

        return self.storage[n]
finish = datetime.datetime.now() - start


start = datetime.datetime.now()

class Factor(object):

    __slots__ = ("storage")

    def __init__(self):
        self.storage = 1

    def __str__(self):
        return f"Factorial of"

    def __call__(self, n):
        start = datetime.datetime.now()

        if n == 0:
            return 1
        else:
            self.storage = n * self.__call__(n-1)


        return self.storage

finish2 = datetime.datetime.now() - start

def main():
    fact = Factor()
    fact2 = Factorial()
    print(fact, "5" , "is" ,fact(5), "time:", finish)
    print(fact, "5" , "is" ,fact2(5), "time:", finish2)


if __name__ == "__main__":
    main()




