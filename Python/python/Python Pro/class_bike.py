class Tire(object):
    def __init__(self):
        self.type_sh = "rez shina"

    

class Frame(object):
    def __init__(self):
        self.type_ram = "alum rama"
    

    
class Bicycle(Tire, Frame):
    def __init__(self):
        super().__init__()
        Frame.__init__(self)

        self.front_tire = self.type_sh
        self.back_tire = self.type_sh
        self.frame = self.type_ram


    def print_specs(self):
        print(f'Рама: {self.frame}')
        print(f'Передняя шина: {self.front_tire}, задняя шина:\
        {self.back_tire}')



if __name__ == '__main__':
    bike = Bicycle()
    bike.print_specs()