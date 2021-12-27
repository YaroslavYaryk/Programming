import re

text = "hey dude, how are you doing"

# print(re.findall(r"are", text))

text = """A blockchain, originally block chain,
is a growing list of records, called blocks,
which are linked using cryptography."""

# print(re.findall(r"b...k", text))
# print(re.findall(r"y.*y", text))
# print(re.findall(r"blocks?", text))

text = "peter piper picked a peck of pickled peppers"
# print(re.findall(r"p.*?e.*?r", text))
text_1 = "crypto-bot that is trading Bitcoin and other currencies"
pattern = re.compile(r"crypto(.{1,30})coin")
# print(pattern.match(text_1))


text = """
"One can never have enough socks", said Dumbledore.
Another Christmas has come and gone and I didn't
get a single pair. People will insist on giving me books."
Christmas Quote
"""
regex = r"Christ.*"
# print(re.findall(regex, text))


page = """
<!DOCTYPE html>
<html>
<body>
<h1>My Programming Links</h1>
<a href="https://app.finxter.com/">test your Python skills</a>
<a href="https://blog.finxter.com/recursion/">Learn recursion</a>
<a href="https://nostarch.com/">Great books from NoStarchPress</a>
<a href="http://finxter.com/">Solve more Python puzzles</a>
</body>
</html>
"""

pattern = r"(<a.*?finxter.com.*(test|puzzle).*?>)"
print(re.findall(pattern, page))