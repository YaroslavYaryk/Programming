from jinja2 import  Template


person = [{"name" : "Yaroslav", "age" : 18, "experience" : 5, "score" : 1000},
          {"name" : "Roma", "age" : 18, "experience" : 3, "score" : 2000},
          {"name" : "Vitalia", "age" : 17, "experience" : 6, "score" : 5000},
          {"name" : "Vasia", "age" : 17, "experience" : 8, "score" : 9000},
          {"name" : "Slava", "age" : 18, "experience" : 11, "score" : 12300}]



#listen to "call_funk"
html = """ 
{%-  macro list_users(listr)  -%}
<ul>
{% for p in listr -%}
    <li>{{p.name}} {{caller(p)}}
{%-  endfor %}
</ul>
{%- endmacro %}


{%- call(user) list_users(users)  %}
    <ul>
        <li> age {{user.age}}
        <li> experience {{user.experience}}   
        <li> score {{user.score}}   
    </ul>  
{% endcall -%} 
"""

temp = Template(html)

msg = temp.render(users = person)

print(msg)
