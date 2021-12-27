def equal_string(a,b):
    if len(a) != len(b):
        return False
    for letter in range(len(a)):
        if a[letter] != b[letter]:
            return False
    return True


def search_substring(a:str, sub:str):
    arr = []

    for i in range(0, len(a) - len(sub)):
        if equal_string(a[i:i+len(sub)] , sub):
            arr.append(i)
    if len(arr) != 0:
        return arr
    return f"it's empty"        

print(search_substring("hellohellohellohello", "ells"))