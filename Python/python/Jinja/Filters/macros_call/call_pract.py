from jinja2 import  Template

person = [{"book" : "Harry Potter", "author" : "J. Rolling", "shits" : 900, "lang" : "english"},
          {"book" : "Tom Soyer", "author" : "M. Tven", "shits" : 800, "lang" : "english"},
          {"book" : "Місто", "author" : "В. Підмогильний", "shits" : 300, "lang" : "українська"},
          {"book" : "Лісова Пісня", "author" : "Л. Українка", "shits" : 100, "lang" : "українська"},
          {"book" : "Чорна Рада", "author" : "П. Куліш", "shits" : 200, "lang" : "українська"}]


html = """

{%- macro list_of_books(books) -%}
<ul>
{% for b in books -%}
    <li> {{b.book}} {{caller(b)}}
    
{% endfor %}
</ul>

{%- endmacro -%}

{% call(user) list_of_books(users) %}
    <ul>
        <li> author - {{user.author}}
        <li> shits - {{user.shits}}
        <li> lang - {{user.lang}}
    </ul>    
{%- endcall -%}
"""

temp = Template(html)
msg = temp.render(users = person)

# print(msg)
with open("call_pract.html", "w",  encoding = "utf-8") as f:
    f.write(msg)