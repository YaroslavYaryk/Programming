from jinja2 import  Template, escape

link = """Link Shows 
<a href="#"<Linker</a> """

"""if we run this we'll see  "Link Shows <a href="#"<Linker</a>" 
that we expect but if we run this n html_file
we'll se completely different 
"<a href="#"<Linker</a>" will convert itno html cod if we wanna ecranize this we have to do following 
if we run this now we'll see "Link Shows &lt;a href=&#34;#&#34;&lt;Linker&lt;/a&gt;" 
that's exactly what we was looking for 
now try to run it as html file we'll get "Link Shows <a href="#"<Linker</a>"  bingo
"""


tm = Template("{{link | e}}") # e - means escape so we dont translate is as html text
output = tm.render(link = link)

print(output)

"""cause this construction is so huge and it does simple process there is class "escape" in Jinja 
so we can use it lite it describe below"""

msg = escape(link)
print(msg) ##we'll get the same result, perfect  and it's the way shorter