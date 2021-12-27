from jinja2 import  Template


# class Person:
    
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
        
#     @property
#     def name(self):
#         return self.__name

#     @property
#     def age(self):
#         return self.__age
        
# pers = Person("Yaroslav", 18)  
pers = {"name" : "Yaroslav", "age" : 18}         
        
      
tm = Template("Hello {{ p.name.title() }}, I know you're {{ p.age }} yers old") #we set exepmlar of class
#as a parametr and call nam and age in our template
rend = tm.render(p = pers)

print(rend)