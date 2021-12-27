for i in range(1,100):
    if i %2 == 0 and i%3 == 0 and i%5 == 0:
        print(i)
        # break  # if there is a break in loop we don't reach else loop
        #but if it's not we get to else block 
else:
    print("get to end")    
    

try:
    1 + 1 # if there is no except situation in try block
except TypeError: # and we get to else block
    print("wrong") #bso,  everyth will work properly

else:
    pass
    # raise TypeError           
    
i = 1    
while i < 100:
    if i %2 == 0 and i%3 == 0 and i%5 == 0:
        print(i)
        break  # if there is a break in loop we don't reach else loop
        #but if it's not we get to else block
    i+=1     
else:
    print("get to end")     