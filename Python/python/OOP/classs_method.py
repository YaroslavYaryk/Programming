class Robot(object):
    population = 0

    def __init__(self,name, age1, age2):
        self.name = name
        self.age1 = age1
        self.age2 = age2
        Robot.population += 1
        print(f"Robot {self.name} was created")


    def destroy(self):
        Robot.population -= 1
        print(f"Robot {self.name} was destroyed")

    def say_hello(self):
        print(f"robot {self.name} says you Welkome") 

    @classmethod
    def how_many(cls):
        print(f"{Robot.population} , we're here")           

class Petrol(object):

    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"robot_age({self.age})"

    @classmethod
    def method(cls, value):
        result = value.age2 + value.age1
        return cls(result)    





r2 = Robot("R2-D2", 22,33) # печатает "Робот R2-D2 был создан"
r2.say_hello() # печатает "Робот R2-D2 приветствует тебя, особь человеческого рода"
Robot.how_many() # печатает "1, вот сколько нас еще осталось"
r2.destroy() # печатает "Робот R2-D2 был уничтожен"
r3 = Petrol(11)
print(r3.method(r2))