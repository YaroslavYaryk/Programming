from jinja2 import  Environment, FileSystemLoader


file_loader = FileSystemLoader("templ")
env = Environment(loader=file_loader)

tmp = env.get_template("main.html")
msg = tmp.render(link = "https://www.youtube.com/watch?v=Ree-JFi06y8", title = "Jinja project")

with open("site.html", "w") as f:
    f.write(msg)