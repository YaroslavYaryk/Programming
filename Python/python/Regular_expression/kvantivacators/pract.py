import re

text = 'aa aba abba abbba abca abea'
match = re.findall(r"ab{1,}a", text) #['aba', 'abba', 'abbba']

match = re.findall(r"ab{,5}a", text) #['aa', 'aba', 'abba', 'abbba']

match = re.findall(r"ab?a", text) #['aa', 'aba']

match = re.findall(r"ab{,5}a", text) #['aa', 'aba', 'abba', 'abbba']

text =  'ab abab abab abababab abea'
match = re.findall(r"[ab]{2,}", text)

text = emails = """zuck26@facebook.com  
page33@google.com  
jeff42@amazon.com""" 

match = re.findall(r"\w+[^@.]", text)
match = re.findall(r"(\w+)@([A-Za-z0-9]+)\.([A-Za-z]+)", text)

text = text = """
Betty bought a bit of butter, 
But the butter was so bitter, 
So she bought some better butter, 
To make the bitter butter better.
"""
match = re.findall(r"[Bb][A-Za-z]+",text)

text = '''Good advice! RT @TheNextWeb:
What I would do differently 
if I was learning to code today
https://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''  

second = re.findall(r".*today", text)
first = re.findall(r".+[^RT]!", text)
match = first + second
strr = " ".join(match)
print(strr)