import re

text = "lat = 5, lon = 3"
match = re.findall(r"\w+\s*=\s*\d+",text)

match = re.findall(r"(lat|lon)\s*=\s*(\d+)",text) #show only if  "key" = "lat" or "lon"

text = "<p>Картинка <img src='bg.img'>в тексті </p>"
match = re.findall(r"<img\s+[^>]*src=[\"'](.+)[\"']", text)
print(match)

match = re.findall(r"<img\s+[^>]*src=([\"'])(.+)\1", text) #means that "\1" is the same as the first backets


print(match)