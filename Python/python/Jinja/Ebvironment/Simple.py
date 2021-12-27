from jinja2 import  Environment, FileSystemLoader 

person = [{"name" : "Yaroslav", "age" : 18},
          {"name" : "Victor", "age" : 28},
          {"name" : "Vova", "age" : 34},
          {"name" : "Symon", "age" : 14},
          {"name" : "Bob", "age" : 11}]

file_loader = FileSystemLoader("")
env = Environment(loader=file_loader)

tm = env.get_template("text.txt")
msg = tm.render(users = person)

with open("env_simp.html", "w",  encoding = "utf-8") as f:
    f.write(msg)
