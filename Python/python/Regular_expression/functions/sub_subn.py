import re

text = "hello world and verybody"

match = re.sub(r"h\w+o", "Hey" , text) #set second argument instead of the first one

text = """Yaroslav
Vova
Andriy
Harold
Neighbor"""

match = re.sub(r"\s*(\w+)\s*", r"<option>\1</option>\n", text )#that's a good one

text = """
<!DOCTYPE html>
<html>
<head>
        Hello world #/////////////////////#
        <base href= "https://www.youtube.com/watch?v=Ree-JFi06y8" >
        <title>Jinja project</title>#/////////////#
        <div class = "dialog" > 
    <p class = "title">Attention</p>
    <p class = "message"></p>#???????????????????#
    <p><input type="button" value="Close"></p>
</div>
</head>##4##########
</html>
"""


match,count = re.subn(r"#.+#", "", text) #deleting comments
print(match, count) #show text and number of changes
text = """<!DOCTYPE html>
<html>
<head>
        Hello world
        <base href= "https://www.youtube.com/watch?v=Ree-JFi06y8" >
        <title>Jinja project</title>
        <div class = "dialog" >
    <p class = "title">Attention</p>
    <p class = "message"></p>
    <p><input type="button" value="Close"></p>
</div>
</head>
</html>
"""

