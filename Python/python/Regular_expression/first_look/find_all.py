import re

"""
REGULAR EXPRESSION

.   - symbol
\d  - any digits  [0-9]
\D  - any non digits
\w  - any Alphabet symbol [A-Z, a-z, 1-9]
\W  - any non alphabet symbols
\s  - breakspace
\S  - non breakspace

'[A-Z][a-z]+' - first letter uppercase, second lovercase to the end of the word

"\w+\.\w+"  - like "gmail.com", "ukr.net"
"""


text = "hello hey hell"

match = re.findall("hel", text) #it finds all the "hel" it this sentence
match = re.findall(r"\bhel\b", text) #it finds all the "hel" it this sentence if there is a word "hel"
#not if this word consist of "hel"
text = "hey hel Hey 55 -4 7 Heo"
match = re.findall(r"[Hh]e[ylo]", text) #first letter is "h" or "H" then "e" next "y" or "L" or "o"
match = re.findall(r"[1-9]", text)#finds all (1-elem) figures in text
match = re.findall(r"[1-9][1-9]", text)#finds all (2-elem) figures in text
match = re.findall(r"[-1-9][1-9]", text)#finds all (2-elem) figures in text (first elem is "-")

match = re.findall(r"[^1-9]", text)#finds all  non  figures in text 
match = re.findall(r"[a-z]", text)#finds all  letters in text 
match = re.findall(r"[^a-zA-Z]", text)#finds all non   letters in text 
match = re.findall(r"[^a-zA-Z1-9]", text)#finds all symbols in text 
match = re.findall(r"\d", text) #all figures in text
match = re.findall(r"\D", text) #all non figures in text
match = re.findall(r"\w", text) #all symbols in text (not spaces etc)
match = re.findall(r"\W", text, re.ASCII) #all symbols only in text 
"""re.ASCII works properly only for English keyboard"""

taxt = "0x4, 0xa, 0x5, 0xf, 0xr"
match = re.findall(r"0x[\da-fA-F]", taxt) #0x than [1-9] or [a-f] or [A-F]


print(match)