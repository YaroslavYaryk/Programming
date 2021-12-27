import re 

text = "hello world aar aejfnvm fjvnfklsv fkjnsm ds "

match = re.findall(r"\w+? ", text)

text =  """zuck26@facebook.com  page33@google.com  jeff42@amazon.com """ 

match = re.findall(r"\w+@\w+\.\w+? ", text) #['zuck26@facebook.com ', 'page33@google.com ', 'jeff42@amazon.com ']
match = re.findall(r"(\w+)@(\w+)\.(\w+)? ", text) #[('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

print(match )