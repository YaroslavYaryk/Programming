from jinja2 import  Environment, FileSystemLoader

members = ["Yarosalv", "Vova", "Andriy", "John", "Marta", "Sarah" ]

file_loader = FileSystemLoader("")
env = Environment(loader=file_loader)

temp = env.get_template("about_it.html") 
msg = temp.render(lister = members)

with open("site_add.html", "w") as f:
    f.write(msg)