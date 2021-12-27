from jinja2 import  Environment, FileSystemLoader

person = [{"name" : "Yaroslav", "age" : 18, "experience" : 5, "score" : 1000},
          {"name" : "Roma", "age" : 18, "experience" : 3, "score" : 2000},
          {"name" : "Vitalia", "age" : 17, "experience" : 6, "score" : 5000},
          {"name" : "Vasia", "age" : 17, "experience" : 8, "score" : 9000},
          {"name" : "Slava", "age" : 18, "experience" : 11, "score" : 12300}]

file_loader = FileSystemLoader("templ")
env = Environment(loader=file_loader)

temp = env.get_template("main.html")
msg = temp.render(users = person)

with open("my_site.html" , "w") as f:
    f.write(msg)