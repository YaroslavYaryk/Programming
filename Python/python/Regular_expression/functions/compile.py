import re

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

rx = re.compile(r"#.+#")
#if we use compile we dont need to put the first argument to (findall, sub, subn...)
print(rx.findall("#jkhkhkkh# dnjdsnkjn #jndjdk#")) #it finds witout fist argument
match,count = rx.subn( "", text) #deleting comments
print(match, count) #show text and number of changes