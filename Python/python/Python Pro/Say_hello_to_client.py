import datetime

class Greeter:

    def __init__(self):
        self.__day = self.__get_day()
        self.__part_of_day = self.__get_part_of_day()
        
        self.__get_part_of_day()

    def __get_day(self):
        return datetime.datetime.now().strftime ('%A')

    def __get_part_of_day(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            day = "morning"
        elif hour > 12 and hour < 17 :  
            day = "day"
        elif hour > 17:
            day = "evening"
        return day    

    def greet(self, store):

        print(f"""Hi, Welcome to {store}!
                wish you happy {self.__day} {self.__part_of_day}!
                Present fot you off 20 %!""")





obj = Greeter()
obj.greet("Coca-cola")