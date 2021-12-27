import re


text = "<option value ='18'>Yaroslav</option>"
match = re.findall(r"value\s*=\s*[\"']\d+[\"']", text)#when i put breckets around something it meants that we
#we wanna ecranize this value if we put "()" arond "\d+" we'll see ['18']
#but if we dont do t we'll get ["value ='18'"]

text = """zuck26@facebook.com  
page33@google.com  
jeff42@amazon.com""" 

match = re.findall(r"(\w+)@(\w+)\.(.+)", text)


print(match) 