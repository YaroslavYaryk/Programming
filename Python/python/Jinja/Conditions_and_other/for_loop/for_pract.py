from jinja2 import  Template, escape 

a = [{"name" : "Yaroslav", "age" : 18},
     {"name" : "Olha", "age" : 16},
     {"name" : "Lida", "age" : 48},
     {"name" : "Yuriy", "age" : 54},
     {"name" : "Maks", "age" : 18},]

link1 =  """<select name="person">
{% for p in person -%} 
    <option value ="{{p["age"]}}">{{p["name"]}}</option>
{% endfor -%}
</select>"""

link2 = """<select name="person">
{% for p in person -%} 
    <option value ="{{p["name"]}}">{{p["age"]}}</option>
{% endfor -%}
</select>"""


temp1 = Template(link1)
temp2 = Template(link2)
output1 = temp1.render(person = a)
output2 = temp2.render(person = a)
print(output1, output2 ,sep = "\n")