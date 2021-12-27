import tkinter as tk
from tkinter import messagebox
import random 

class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.a = None
        self.lable11 = None
        self.storage = ["red", "orange", "yellow", "green", "blue", "purple"]


    def run(self):
        self.drow_label()
        self.push_button()
        self.root.mainloop()


    def make_right_choice(self,color):
        if color == self.a:
            choice = messagebox.askyesno("continue", "You won, wanna continue???")
            if not choice:
                self.root.destroy()
            else:
                self.a = random.choice(self.storage)
                self.lable1.configure(text = self.a, bg = self.a)

        else:
            messagebox.showerror("error", "Wrong answer")
            
            self.a = random.choice(self.storage)
            self.lable1.configure(text = self.a, bg = self.a)
               





    def push_button(self):
        pass
        tk.Button(self.root, text="red", width = 20, height = 2, bg = "red", command = lambda: self.make_right_choice("red")).pack()
        tk.Button(self.root, text="orange", width = 20, height = 2, bg = "orange", command = lambda: self.make_right_choice("orange")).pack()
        tk.Button(self.root, text="yellow", width = 20, height = 2, bg = "yellow", command = lambda: self.make_right_choice("yellow")).pack()
        tk.Button(self.root, text="green", width = 20, height = 2, bg = "green", command = lambda: self.make_right_choice("green")).pack()
        tk.Button(self.root, text="blue", width = 20, height = 2, bg = "blue", command = lambda: self.make_right_choice("blue")).pack()
        tk.Button(self.root, text="purple", width = 20, height = 2, bg = "purple", command = lambda: self.make_right_choice("purple")).pack()


    def drow_label(self):

        self.a = random.choice(self.storage)
        self.lable1 = tk.Label(self.root, text =  self.a,
                        activebackground = "purple",
                        activeforeground = "white",
                        highlightcolor = "pink",
                        background = self.a,
                        padx = 5,
                        pady = 5,
                        font = ("Arial", 15, "bold"))
        self.lable1.pack()                 

        return self.a, self.lable1
                          




    def exit(self):
        choise =messagebox.askyesno("quit", "Sure you wanna quit?")
        if choise:
            self.root.destroy()

win = Window("My program", 500, 500, "pink", (True, True))  
win.run()