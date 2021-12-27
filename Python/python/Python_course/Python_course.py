class Book(object):
    __slots__ = ("author", "name", "year", "genre")

    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.author == other.author and \
            self.name == other.name and \
            self.year == other.year and \
            self.genre == other.genre

    def __str__(self):
        return f"{self.author}  {self.name}  {self.year}  {self.genre}"


book = Book("Dyknanov", "the adventure of my life", 2020, "horror")
kook = Book("Dyknanov", "the adventure of my life", 2020, "horror")

print(book)
print(kook)
print(book == kook)