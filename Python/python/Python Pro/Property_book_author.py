class Author(object):

    def __init__(self, data_author):
        self.first_name = data_author["name"]
        self.last_name = data_author["last name"]


    @property
    def for_display(self):    
        return f"{self.first_name} {self.last_name}"
    @property
    def for_citation(self):
        return f"{self.last_name} {self.first_name[0]}."


class Book:
    def __init__(self, data):

        self.author_data = data['Author']
        self.author = Author(self.author_data)

    @property
    def author_for_display(self):
        return self.author.for_display

    @property
    def author_for_citation(self):
        return self.author.for_citation    



dictionary = {"Author": {
            "name" : "Yaroslav",
            "last name" : "Dyhanov"}}

book = Book(dictionary)      
print(book.author_for_display)  
print(book.author_for_citation)      
