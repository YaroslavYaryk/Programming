class No_negative():
    
    def __set_name__(self, owner, name):
        self.__name = name
    
    def __get__(self, instance, owner):

        return instance.__dict__[self.__name]
    
    def __set__(self, instance, value):
        
        if isinstance(value, (int, float)):
            if value > 0:
                instance.__dict__[self.__name] = value
            else:
                raise ValueError("can't be negative") 
        else:
            raise TypeError("can only work with integer or float")                          

class Integers:
    
    first = No_negative()
    second = No_negative()
    
    def __init__(self, first, second):
        self.first= first
        self.second = second
        
        
    def __str__(self):
        return f" Marka - {self.first}  Model - {self.second}"
    
    
if __name__ == "__main__":    
    ford = Integers(-12 , 123)
    print(ford.first, ford.second)
    # print(ford)                