import re


text = """
<!DOCTYPE html>

<html>
<body>
    <head>
        Hello world
        <title>My_site</title>
    </head>
    <ul>
        <li> Yaroslav  <ul>
            <li> age 18
            <li> experience 5
            <li> score 1000

        </ul><li> Roma  <ul>
            <li> age 18
            <li> experience 3
            <li> score 2000

        </ul><li> Vitalia  <ul>
            <li> age 17
            <li> experience 6
            <li> score 5000

        </ul><li> Vasia  <ul>
            <li> age 17
            <li> experience 8
            <li> score 9000

        </ul><li> Slava  <ul>
            <li> age 18
            <li> experience 11
            <li> score 12300

        </ul></ul>
        

    <div class = dialog > 
    <p class = "title">Warning</p>
    <p class = "message"></p>
    <p><input type="button" value="Close"></p>
</div></body>
</html>"""

match = re.findall(r"<head>([\w\W]+)(?=</head>)", text) #['\n        Hello world\n        <title>My_site</title>\n    ']
#"?=" - till to ...
match = re.findall(r"<head>([\w\W]+)(?<=</head>)", text) #['\n        Hello world\n        <title>My_site</title>\n    </head>']
#"?<=" - till to and including the last character

match = re.findall(r'''[-\w]+[\t ]*=[\t ]*[\""]\w+[\""]''', text)#['class = "dialog"', 'class = "title"', 'class = "message"', 'type="button"', 'value="Close"']
match = re.findall(r'''([-\w]+)[\t ]*=[\t ]*[\""?]([\w ]+)[\""]''', text)#[('class', 'dialog'), ('class', 'title'), ('class', 'message'), ('type', 'button'), ('value', 'Close')]
match = re.findall(r'''([-\w]+)[\t ]*=[\t ]*["]?([\w ]+)["]?''', text)#[('class', 'dialog '), ('class', 'title'), ('class', 'message'), ('type', 'button'), ('value', 'Close')]
"""select key = "value" or key = value
with лапками and without"""


text = "Python, python, PYTHON"
match = re.findall(r"(?i)python", text)
#(?...) - flag
#(?i)  ignore case


print(match)