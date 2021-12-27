from datetime import  datetime

now = datetime.now()
print(now)# if we jyst call now we'll get  2021-04-20 21:36:56.817400
print(format(now, "%H:%M:%S"))  # but if we do this operation we'll get 21:36:56

print(format(42, "b")) #get binary version of 42
# print(format(42, "he"))
# print(format(42, "b"))


print(format(2/3, ".1%")) #if wu dont use "%" we get "0.7"
#but if we use we get 66.7% 