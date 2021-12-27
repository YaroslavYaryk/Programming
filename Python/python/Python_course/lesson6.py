first = input("enter first:")
second = input("enter seconf:")



storage = set()
def Common(first, srcond):
    
    for letter in range(len(first)):
        if first[letter] in second:
            storage.update(first[letter])
        else:
            continue    
    return storage

print(Common(first,second))



