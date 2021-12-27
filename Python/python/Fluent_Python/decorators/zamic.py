def coll():
    count = 0
    total = 0

    def inner(value):
        nonlocal count
        nonlocal total
        count+=1
        total += count* value
        # print(count/5)
        return total
    return inner

a = coll()
print(a(10))    