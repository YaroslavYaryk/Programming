from no_negatie import No_negative

class Point:
    # __x = No_negative()
    # __y = No_negative()
    
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    

class Rectangle():
        
    
    def __init__(self, x1, y1, x2, y2) :
        self.__coard_x = Point(x1, y1)
        self.__coard_y = Point(x2, y2)
    
    def __str__(self):
        return f"({self.__coard_x}, {self.__coard_y})" 
    
    @property
    def coard_x(self):
        return self.__coard_x
    
    @coard_x.setter
    def coard_x(self, *args):
        self.__coard_x = Point(args[0][0], args[0][1])
        
    @property
    def coard_y(self):
        return self.__coard_y
    
    @coard_y.setter
    def coard_y(self, *args):
        self.__coard_y = Point(args[0][0], args[0][1])     
    
        
rect = Rectangle(1,2,3,4)
print(rect)           
rect.coard_x = 11, 22
rect.coard_y = 33, 44
print(rect)           

           
    
        
        