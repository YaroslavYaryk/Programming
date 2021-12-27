from jinja2 import  Template


a = [{"marka" : "Ford", "price" : 2500},
     {"marka" : "Volvo", "price" : 3500},
     {"marka" : "Honda", "price" : 4500},
     {"marka" : "Ferrari", "price" : 55500},
     {"marka" : "Fiat", "price" : 5500}]


lister = [2,3,1,4,3,1,5,3]

temp = Template("Total price of cars is {{cars | sum(attribute = 'price')}} ")
#calculate total price of the cars {{collection | method }}
msg = temp.render(cars = a)

temp = Template("sum is  {{listt | sum}}") #sum of array
msg = temp.render(listt = lister)

temp = Template("sum is  {{listt | sort}}") #sort the  array
msg = temp.render(listt = lister)

temp = Template("Total price of cars is {{(cars | max(attribute = 'price')).marka }} ") # car wit the biggest price
msg = temp.render(cars = a)

temp = Template("random:  {{cars | random }} ") # get random dict
msg = temp.render(cars = a)

temp = Template("Cars:  {{cars | replace('o', 0 ) }} ") # replace all the "o" letters to 0
msg = temp.render(cars = a)

print(msg)