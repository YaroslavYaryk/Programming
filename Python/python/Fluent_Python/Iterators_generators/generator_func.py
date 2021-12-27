import re
import reprlib

RE_WORD = re.compile("\w+")

class Sentence():

    def __init__(self, text):
        self.text = text

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))   

         

    def __repr__(self):
        return f"Sentence {reprlib.repr(self.text)}"    
        




a = Sentence("hello world and everybody")

for i in a:
    print(i)
