import re


text = "Google Gooogle  Gooooooogle"

match = re.findall(r"o{2,5}",text ) #find all "o" that count = (from 2 to 5) (Major - takes max if it's possible)
match = re.findall(r"o{2,5}?",text ) #find all "o" that count = (from 2 to 5) (Minor - takes min ("oo" * n) if it's possible)


match = re.findall(r"Go{2,7}gle", text) #"G" + "o" * (2,5) + gle
match = re.findall(r"Go{,5}gle", text) #"G" + "o" * (0,5) + gle (max is "o" * 5)
match = re.findall(r"Go{1,}gle", text) #"G" + "o" * (0,5) + gle (min is "o" * 1, max is inf)

text = "Simpple, Simple"
match = re.findall(r"Simpp?le", text)#takes "pp" or "p"
""" ? = {1,2} 
    * = {0,inf}
    + = {1,inf}
"""

text = "author=Підмогильний В.; title = Місто; price = 500; year = 1927"
match = re.findall(r"\w+\s*=\s*[^;]+", text)

text = "<p>Картинка <img src='bg.img'>в тексті </p>"
match = re.findall(r"<img.*>",text ) 
"""it finds max sequences so it'll be found #["<img stc='bg.img'>в тексті </p>"] 
if we wanna find till first ">" we should use minor kvant (?)
or re.findall(r"<img[^>]*>",text ) """

match = re.findall(r"<img.*?>",text ) 
match = re.findall(r"<img[^>]*>",text ) 

text = "<p>Картинка <img src='bg.img'>в тексті </p>"
match = re.findall(r"<img\s+.*src\s*=\s*[^>]+>",text ) 

text = """ djhdskfhskjdfhdsf #hello
            gfjfkdhvkjdfvkjdfkjvfkd #world
            jhskjfhksjdhfkdshfkdshf #and
            hfksdhfksdhfsdkhkshkkfshfhksh #everybody"""

match = re.findall(r"#.*", text)

print(match)