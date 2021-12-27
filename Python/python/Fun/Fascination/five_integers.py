def get_sume(num):
    a = sum([int(i) for i in str(num)])
    while  a > 9:
        a = sum([int(i) for i in str(a)])
    else:
        print(a)
        
get_sume(12333333336547896542)            
        
    
    