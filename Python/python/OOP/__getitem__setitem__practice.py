class Timme(object):

    __slots__ = ("second")

    def __init__(self, second):
        self.second = second

    def __getitem__(self, key):

        if isinstance(key, str):
            if key == "hour":
                return (self.second // 3600)
            elif key == "minute":
                return (self.second // 60)
            elif key == "doba":
                return ((self.second // 3600) // 24)
            else:
                raise KeyError("not such keys")

        else:
            raise ValueError("key must be str")

    def __setitem__(self, key, value):

        if not isinstance(key, str):
            raise ValueError("key must be only str")
        else:
            hour = self.second // 3600
            minute = self.second // 60
            doba = (self.second // 3600) % 24

        if key == "minute":
            return value * minute + hour * 3600 + doba * 86400
        elif key == "hour":
            return minute + value*hour * 3600 + doba * 86400
        elif hey == "doba":
            return minute + hour * 3600 + value * doba * 86400
        else:
            raise KeyError("none such key")


# timmy = Timme(11000)
# print(timmy["doba"])


class Book(object):

    def __init__(self):
        self.book_mark = {"Dyhanov": "My story",
                          "Roberto": "Advantures of me",
                          "Dionos": "Life in a year"}

    def __printa(self, key):
        return f"The book that was written by <{key}> is '{self.book_mark[key]}'"

    def all_print(self):
        for key in self.book_mark:
            print(key, "-", self.book_mark[key])

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise KeyError("key must be string")
        elif key in self.book_mark:
            return Book.__printa(self, key)
        else:
            raise KeyError("none of such key")

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise KeyError("key must be string")
        else:
            self.book_mark[key] = value


writer = Book()
print(writer["Dyhanov"])
writer["Malorok"] = "Story of my life"
writer["Dyhanov"] = "My fucking cool life"
writer.all_print()
print(writer["Malorok"])
