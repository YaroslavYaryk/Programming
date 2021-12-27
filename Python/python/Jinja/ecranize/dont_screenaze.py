from jinja2 import  Template

        
pers = {"name" : "Yaroslav", "age" : 18}         
        
      
tm = Template("{% raw %} Hello {{ p.name.title() }}, I know you're {{ p.age }} yers old {% endraw %}") 
#if we dont wanna translate (p.name) we can use {% raw %} ... {% endraw %} #
# to hide translation it's gonnabe like: 
""" Hello {{ p.name.title() }}, I know you're {{ p.age }} yers old """
rend = tm.render(p = pers)

print(rend)