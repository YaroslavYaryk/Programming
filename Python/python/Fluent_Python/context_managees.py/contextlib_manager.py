from contextlib import contextmanager
import sys

@contextmanager
def Looking_glass():
    original_write = sys.stdout.write
    
    def reversed_text(text):
        original_write(text[::-1])
    sys.stdout.write = reversed_text
    msg = ""
    try:
        yield "JABBERWOCKY"
    except Exception as ex:
        msg = ex
    finally:        
        sys.stdout.write = original_write
        if msg:
            sys.stdout.write(msg) 
                  
with Looking_glass() as what:
    print("hello world")
    print(what)    

    