def simple_continue():
    print("continue...")
    x = yield
    print("received: ", x)
    
my_dec = simple_continue()
# (next(my_dec)) 
# my_dec.send(42)   
# (next(my_dec))    

def simple_continue(a):
    print("continue...", a)
    b = yield a
    print("received: ", b)
    c = yield a + b
    print("received: ", c)
    
my_dec = simple_continue(14)
(next(my_dec)) 
my_dec.send(42)
my_dec.send(99)   
   

# (next(my_dec)) 

  
  
