def get_aver():
    totl = 0.0
    count= 0
    average = None
    while True:
        term = yield average
        totl += term
        count += 1
        average = totl/count
        

k = get_aver() 
next(k)
print(k.send(10))   
print(k.send(30))       
print(k.send(5))       
    