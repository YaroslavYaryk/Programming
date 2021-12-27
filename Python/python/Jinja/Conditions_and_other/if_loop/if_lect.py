from jinja2 import  Template, escape 

a = [{"name" : "Yaroslav", "age" : 18},
     {"name" : "Olha", "age" : 16},
     {"name" : "Lida", "age" : 48},
     {"name" : "Yuriy", "age" : 54},
     {"name" : "Maks", "age" : 18},]

link1 =  """<select name="person">
{% for p in person -%} 
    {% if p.age >= 18  -%}
        {% if p.name == "Yaroslav" -%}
            <option>{{p["name"][::-1]}}</option>
        {% else -%}    
            <option value = {{p["age"]}}>{{p["name"]}}</option>
        {% endif -%}   
    {% else -%}
        {{p.name}}
    {% endif -%}    
{%- endfor -%}
</select>"""

temp1 = Template(link1)
output1 = temp1.render(person = a)
print(output1)

