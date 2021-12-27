import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence():

    def __init__(self, text):
        self.text = text
        self.__words = text.split()

    def __iter__(self):
        return Sentence_Iterator(self.__words)    

    # def __getitem__(self,index):
    #     return reprlib.repr(self.__words[index])


    def __len__(self):
        return len(self.__words)           

    def __repr__(self):
        return f"Sentence {reprlib.repr(self.text)}"    
        

class Sentence_Iterator:

    def __init__(self, words):

        self.words = words
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = reprlib.repr(self.words[self.index])
        except IndexError:
            raise StopIteration()

        self.index += 1
        return word    





a = Sentence("hello world and everybody")

for i in a:
    print(i)
