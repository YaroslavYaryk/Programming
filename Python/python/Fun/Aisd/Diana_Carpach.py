class Color:
    
    __colors = ("black", "white", "red", "blue", "green", "yellow", "brown")
    
    def __init__(self):
        self.__color = "black"
        
    
    @property
    def color(self):
        return self.__color
    
    @color.setter 
    def color(self, value):
        if value.lower() in Color.__colors:
            self.__color = value
        else:
            raise ValueError("Wrong type of value")



colors = Color()
print(colors.color)     
colors.color = "WHite"          
print(colors.color)     
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    