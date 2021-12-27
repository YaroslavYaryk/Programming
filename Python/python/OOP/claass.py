class Point:

    __slots__ = ("__Xa", "__Ya")

    def __init__(self, Xa, Ya):
        self.__Xa = Xa
        self.__Ya = Ya

    def __str__(self):
        return f"({self.__Xa} {self.__Ya})"


class One:
    def __init__(self):
        print("One")
        super().__init__()


class Two:
    def __init__(self):
        print("Two")
        super().__init__()



class Three(One, Two):

    __slots__ = ("_x", "_y", "_color")

    def __init__(self, x: Point, y: Point, color="red", ):
        self._x = x
        self._y = y
        self._color = color
        super().__init__()

    def drow(self):
        print(f"{self._x} {self._y} {self._color}")


object = Three(Point(10, 20), Point(11, 21), "green")
object.drow()
