class Desk():
    
    def __init__(self, name):
        self.__name = name
    
    def __get__(self, instance, owner):

        return instance.__dict__[self.__name]
    
    def __set__(self, instance, value):
        
        instance.__dict__[self.__name] = value
        
        
class Car:
    
    marka = Desk("marka")
    model = Desk("model")
    
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        
        
    def __str__(self):
        return f" Marka - {self.marka}  Model - {self.model}"
    
    
ford = Car("Ford", "Escort")
print(ford.model)
# print(ford)                