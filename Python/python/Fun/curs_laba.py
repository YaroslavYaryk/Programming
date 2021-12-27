from time import sleep
a = [[34,21,32,41,25],
    [14,42,43,14,31],
    [54,45,52,42,23],
    [33,15,51,31,35],
    [21,52,33,13,23]]

def funk(a:list, operation = "work"):
    start = a[0][0]
    des_pos = start//10
    od_pos = start%10
    printa(a, des_pos-1, od_pos-1)
    count = 0
    while a[des_pos-1][od_pos-1] != des_pos*10 + od_pos :
        start = a[des_pos-1][od_pos-1]
        des_pos = start
        od_pos = start%10
        if operation == "check":
            # global count
            count+=1
            if count == 100:
                return False
        elif operation == "work":        
            printa(a, des_pos-1, od_pos-1)
            sleep(2)
    else:
        if operation == "check":
            return True           
        print("found it ") 
        print(a[des_pos-1][od_pos-1])    

def printa(a:list, des:int, od:int):

    print("\n+----++----++----++----++----+")    
    for i in range(5):
        for j in range(5):
            if i == des and j == od:
                print(f"|*{a[i][j]}*|", end = "")
                continue
            else:
                print(f"| {a[i][j]} |", end = "")
        print("\n+----++----++----++----++----+")    


def is_true(a:list):
    for i in range(5):
        for j in range(5):
            if a[i][j] == (i+1)*10 + (j+1):
                return True
    return False    


def main():
    choice = input("wanna start? ")
    if choice =="Yes" or choice == "yes" or choice == "1":
        if is_true(a) and funk(a,"check") :
            funk(a)
        else:
            print("sorry but  can't find treasure element")    


if __name__ == "__main__":
    main()