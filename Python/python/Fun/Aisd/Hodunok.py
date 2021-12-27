import math

x = int(input("enter x: "))
y = 0
if x > 0:
    y = math.sin(2*x) - 7
elif x == 0:
    y = math.cos(2*x)**2 + 14
else:
    y = round(2*x+3)
print(y)            
    