from Examples_deskriptors import NonNegative
class Calendar(object):

    __slots__ = ("_day", "_month", "_year",  "__storage")

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year

    @property
    def changed(self):
        return (self._day, self._month, self._year)

    @changed.setter
    def changed(self, *args):
        self.__storage = []
        for i in args:
            for g in i:
                self.__storage.append(g)

        if len(self.__storage) == 3:
            self._day = self.__storage[0]
            self._month = self.__storage[1]
            self._year = self.__storage[2]
        else:
            raise ValueError("Invalid")


point = Calendar(31,3, 2003)
print(point.changed)
point.changed =1,2,3
print(point.changed)


class Check_int_float(object):

    @staticmethod
    def __checker(value):
        return isinstance(value, (int, float))

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if Check_int_float.__checker(value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError


class Rectangle(object):

    __coard_one = Check_int_float()
    __coard_two = Check_int_float()

    def __init__(self, coard_one, coard_two):
        self.__coard_one = coard_one
        self.__coard_two = coard_two

    def gettt(self):
        return self.__coard_one, self.__coard_two


rect = Rectangle(11, 22)
print(rect.gettt())


class Important_files(object):
    @staticmethod
    def __IsInt(value):
        return isinstance(value,int)

    def __set_name__(self,owner,name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        
        if Important_files.__IsInt(value):
            instance.__dict__[self.name] = value
            with open("lol.txt", "w") as f:
                f.write(str(value) + ",\n")
                    


class List_of_marks(object):

    mark = Important_files()
    mark = NonNegative()

    def __init__(self, mark):
        self.mark = mark
 
skf = List_of_marks(22)
some = List_of_marks(11)
with open("lol.txt", "r") as f:
    print(f.read())