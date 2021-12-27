from jinja2 import  Template


Sale = [{"marka" : "Ford", "price" : 2500},
     {"marka" : "Volvo", "price" : 3500},
     {"marka" : "Honda", "price" : 4500},
     {"marka" : "Ferrari", "price" : 55500},
     {"marka" : "Fiat", "price" : 5500}]




#show all anmes of marks in uppercase
arr = """ 
{% for c in lisr -%}
    {% filter upper -%}{{c.marka }}\n{%  endfilter-%}
    
{% endfor -%}    
"""


temp = Template(arr)
msg = temp.render(lisr = Sale)


print(msg)