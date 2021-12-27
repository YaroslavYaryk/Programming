def deco(funk):
    
    print("hello")
    return funk

@deco
def say_hello(*args):
    print("hello world")

say_hello()    