from jinja2 import  Template, escape 


dictionary = [{"subject" : "math", "mark" : 5 },
              {"subject" : "history", "mark" : 4 },
              {"subject" : "literature", "mark" : 4 },
              {"subject" : "physics", "mark" : 5 },
              {"subject" : "english", "mark" : 5 }]



link = """ <select name = "pupil">
{% for p in pupil -%}
    {% if p.mark > 4 -%}
        <option value = {{p.mark}}>{{p.subject}} </object>
    {% else -%}
        <option value = {{p.mark-1}}>{{p.subject + " lol" }} </object>
    {% endif -%}
{% endfor -%}
</select>        
"""

temp = Template(link)
message = temp.render(pupil = dictionary)

print(message)