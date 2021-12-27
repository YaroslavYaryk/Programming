class Book(object):

    def __init__(self, data):
        self.title = data["Title"]
        self.subtitle = data["Subtitle"]

    @property
    def display_title(self):
        if self.title and self.subtitle:
            return f"{self.title} : {self.subtitle}"
        elif self.title:
            return self.title
        else:
            return "Untitled"            

data = {"Title" : "My job",
        "Subtitle" : "software development"}            

book = Book(data)
print(book.display_title)        