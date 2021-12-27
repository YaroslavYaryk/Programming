import tkinter as tk
import all_list
import chosen_elements
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])


    def run(self):
        self.drow_button()
        self.root.mainloop()

    def sign_in(self):

        self.get_child( all_list,"all_list", 200,370, "#5199FF")
        

    def sign_up(self):

        self.get_child( chosen_elements,"chosen_elements", 200,400, "#5199FF")
    


    def drow_button(self):

        tk.Button(self.root, text="range", command = self.sign_in, width = 20,activebackground = "red", font = ("Arial", 14), height = 3,bg = "yellow", fg = "green").pack(pady = 20)
        tk.Button(self.root, text="chosen_elements",width = 20, command = self.sign_up, activebackground = "red", font = ("Arial", 14), height = 3,bg = "yellow", fg = "green").pack(pady = 20)



    def get_child(self, child ,title , height, width, bg_color , resizable = (False, False)):
        child.ChildWindow(self.root, title, height, width, bg_color, resizable)  





win = Window("My program", 250, 250, "green", (True, True))  
win.run()
