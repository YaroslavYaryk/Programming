
def binary_search_rec(lister, start, end, item):
    
    mid = (start + end )//2

    if lister[mid] == item:
        return mid
    elif lister[mid] > item:
        return binary_search(lister, 0, mid, item) 
    else:
        return binary_search(lister, mid, len(lister), item)



def binary_search(lister, item):

    

my_list = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(my_list, 0, len(my_list), 11))                