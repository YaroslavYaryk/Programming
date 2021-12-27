from jinja2 import  Template, escape 

cities = [{"id" : 1, "city" : "Kyiv"},
          {"id" : 3, "city" : "Lviv"},
          {"id" : 5, "city" : "Rivne"},
          {"id" : 7, "city" : "Lutsk"},
          {"id" : 9, "city" : "Varash"},
          {"id" : 11,"city" : "Sarny"},]

link = """<select name="cities">
{% for c in cities -%} 
    <option value ="{{c["id"]}}">{{c["city"]}}</option>
{% endfor %}
</select>"""

#should not forget about "-%" its for not seeing "\n" all the time 

"""this for loop allow us to make the sane way as simpe for loop
we go over array and do someth we wanna do"""

tm = Template(link)
msg = tm.render(cities = cities)
print(msg)