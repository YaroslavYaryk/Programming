def null(num):
    counter = 0
    lists = [x for x in str(num)]
    pos  = len(lists) - 1
    while int(lists[pos]) == 0:
        counter += 1
        pos -=1

    print(counter)

null(100)    