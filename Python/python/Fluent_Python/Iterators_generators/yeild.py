def gener(*iterables): # if we use this we have to build one more 'for' loop 
    for i in iterables: # to iterae by charachter
        for e in i:
            yield e
        
        
a = gener("hello") 
print(list(a))

def gener(*iterables): #but we can use yeild from to avert this operation 
    for i in iterables: 
       yield from i
       
a = gener("hello") 
       
print(list(a)) #the same result
       
        
        