import random
import time
string="qwertyuiop[[]asdfghjkl;'zxcvbnm1234567890-="
string = "Hlwlorde "
targer_array = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]
string_array = ["", "", "", "", "", "", "", "", "", "", ""]   

x=0
while x < len(string_array):
    string_array[x] = random.choice(string)
    if string_array[x] != targer_array[x]:
        print(string_array[x] +  '\b', end="")
    else:
        print(string_array[x] , end="")
        x+=1    
    time.sleep(0.01)
