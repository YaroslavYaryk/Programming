from jinja2 import  Template


#as we all know we have to follow DRY(dont repite yourself )
#we can use macros like it's writes above 
#we create macros "input" and descibe it like we describe a class
#and then we use it 
html = """
{%-  macro  input(name, value = "", type = "text", size = 20) -%}
<input type = "{{type}}" name = "{{name}}" value = "{{value}}" size = "{{size}}">
{%- endmacro -%}

<p>{{input("username")}}
<p>{{input("mail")}}
<p>{{input("password")}}
"""



temp = Template(html)
msg = temp.render()

with  open("macr.html", "w",  encoding = "utf-8" ) as f:
    f.write(msg)
# print(msg)