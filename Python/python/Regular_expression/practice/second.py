import re 

file = ""
with open("second.html", "r") as f:
    file = f.read()
    
result = re.findall(r"[\w._-]+@[\w._].[\w.]+", file) 
# result = re.findall(r"[a-zA-Z]+\s\w+\.\s\w+", file) 

with open("result.txt", "w") as f:
    f.write("\n".join(result))   