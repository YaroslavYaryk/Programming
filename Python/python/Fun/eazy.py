f=(input("введите 1 что бы прибывить, 2 что бы отнять, 3 умножить, 4 разделить: "))
a=(input("введите первое число:  "))
b=(input("введите второе число:  "))
if f.isdigit() and f in ["1", '2', "3", "4"]:
    
    if a.isdigit():
        a=int(a)
    if b.isdigit():
        b=int(b)
    if(f)==("1"):
            print((a)+(b))
    elif(f)==("2"):
            print((a)-(b))
    elif(f)==("3"):
            print((a)*(b))
    elif(f)==("4"):
            print((a)/(b))
else:
    print("вы ввели что то другое")