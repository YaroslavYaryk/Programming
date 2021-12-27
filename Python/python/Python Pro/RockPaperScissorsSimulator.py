import random

class Game:

    def __init__(self):
        self.OPERATIONS = ["Камінь", "Ножниці" , "Папір"]
        self.computer_choice = None
        self.human_choice = None
        self.computer_make_choice()
        self.person_make_choice()


    def computer_make_choice(self):
        self.computer_choice =random.choice(self.OPERATIONS)

    def person_make_choice(self):
        print("Камінь ", "Ножниці", "Папір")
        self.human_choice = input(":")

    def print_choices( self,):

        print(f"computer's choise is {self.computer_choice}")
        print(f"person's choise is {self.human_choice}")


    def __win_lose_funk(self, win_oper, lose_oper):

        if self.computer_choice == win_oper:
            print("computer Won")
        elif self.computer_choice == lose_oper:
            print("computer Lost")
        elif self.computer_choice == self.human_choice:
            print("Nobody Won")       

    def main_win_lose_funk(self):

        if self.human_choice == "Камінь":
            self.__win_lose_funk( "Папір", "Ножиці")
        elif self.human_choice == "Ножиці":
            self.__win_lose_funk( "Камінь", "Папір")
        elif self.human_choice == "Папір":
            self.__win_lose_funk( "Ножиці", "Камінь")

obj = Game()

obj.print_choices()
obj.main_win_lose_funk()