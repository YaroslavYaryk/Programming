from jinja2 import  Environment, FileSystemLoader

books = [{"book" : "Harry Potter", "author" : "J. Rolling", "shits" : 900, "lang" : "english"},
          {"book" : "Tom Soyer", "author" : "M. Tven", "shits" : 800, "lang" : "english"},
          {"book" : "Місто", "author" : "В. Підмогильний", "shits" : 300, "lang" : "українська"},
          {"book" : "Лісова Пісня", "author" : "Л. Українка", "shits" : 100, "lang" : "українська"},
          {"book" : "Чорна Рада", "author" : "П. Куліш", "shits" : 200, "lang" : "українська"}]


file_loader = FileSystemLoader("")
env = Environment(loader=file_loader)

tmp = env.get_template("about_main.html")
msg = tmp.render(users = books )

with open("pract_add.html", "w", encoding="utf-8") as f:
    f.write(msg)