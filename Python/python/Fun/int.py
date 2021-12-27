a = int(input("num: "))
b = int(input("base: "))
pos = 0
while True:
    try:
        pos += 1
        int(str(pos), base = b) == a
        

    except Exception:
        continue

    else:
        break    


print(pos)