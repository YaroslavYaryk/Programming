import sys

class Looking_class:
    
    def __enter__(self):
        self.original_white = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return "JABBERWOCKY"
    
    def reverse_write(self, text):
        self.original_white(text[::-1])
        
    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout.write = self.original_white
        if exc_type is ZeroDivisionError:
            print("please, don't divide by zero")
            return True
        
        
with Looking_class() as what:
        print("hello world")
        print(what)            
        
        
