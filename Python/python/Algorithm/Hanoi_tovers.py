def hanoi(n,i,k):
    if n == 1:
        print(f"move disk 1 from {i} to {k} ")
    else:
        tmp = 6 - i - k
        hanoi(n-1,i,tmp)
        print(f"move disk {n} from {i} to {k} ")
        hanoi(n-1 , tmp, k)    

hanoi(3,1,2)        