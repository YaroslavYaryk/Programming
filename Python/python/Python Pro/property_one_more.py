class Temperature(object):

    def __init__(self, temp = 0):
        self.__temperature = temp

    def go_farengait(self):
        return round(self.__temperature * 1.8, 2) + 32

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("temperature must be above tnan -273")
        else:
            self.__temperature = value

temp = Temperature(37)
print(temp.temperature) 
print(temp.go_farengait())   
temp.temperature = 20
print(temp.temperature) 
print(temp.go_farengait())   



