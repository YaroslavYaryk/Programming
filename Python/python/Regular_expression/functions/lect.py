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
   
</div></body>
</html>"""
text = "<div class = dialog >"
match = re.search(r'(\w+)\s*=\s*["]?(\w+)["]?', text)
# print(match)
# print(match.groups()) #create group (0 - all character) (1 - first breckets) (2 - second breckets)
#if its more than one group gets only first
# (match.groups())#show element of first group
print(match.start(1) ) #index of start of the first group
print(match.end(1) ) #index of end of the first group
print(match.expand(r"\1:\2")) #show  first group then ":" then second group
 
