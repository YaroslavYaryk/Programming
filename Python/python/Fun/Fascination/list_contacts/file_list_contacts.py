
a = ""
with open("file.txt", "r") as f:
    a = f.read()
    # for i in a:
    #     k = " ". join(i)

a = a.split("\n")
e = ""
d = {}

for i in a:
    k = " ".join(i)

for i in a:
    for j in i:
        if j =="-":
            continue
        else:
            e +=j
e = e.split("  ")    
for i in range(1,len(e)-1,2):
    d[e[i]] = e[i-1]
    
with open("file.txt", "w") as f:
    # for i in sorted(d):
    f.write(str(d[380684862861]))
    
            
    # print(i, d[i])   