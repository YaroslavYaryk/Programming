setter = set()

def deco(active = True):

    def devorate(funk):
        
        if active:
            setter.add(funk)
        else:
            setter.discard(funk)
        return funk    

    return devorate 

@deco()
def print_hello():
    print("hello world")

(print_hello()) 
(print_hello()) 

print(setter)   


