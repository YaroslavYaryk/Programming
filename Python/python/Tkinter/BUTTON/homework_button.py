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
        self.lable1 = tk.Label(self.root, width = 12, text =  "red", bg = "red", font = ("Arial", 15, "bold"))
        self.lable2 = tk.Label(self.root, width = 12, text =  "orange", bg = "orange", font = ("Arial", 15, "bold"))
        self.lable3 = tk.Label(self.root, width = 12, text =  "yellow", bg = "yellow", font = ("Arial", 15, "bold"))
        self.lable4 = tk.Label(self.root, width = 12, text =  "green", bg = "green", font = ("Arial", 15, "bold"))
        self.lable5 = tk.Label(self.root, width = 12, text =  "blue", bg = "blue", font = ("Arial", 15, "bold"))
        self.lable6 = tk.Label(self.root, width = 12, text =  "purple", bg = "purple", font = ("Arial", 15, "bold"))
        self.color_storage = ["red", "orange", "yellow", "green", "blue", "purple"]
        self.storage = [self.lable1, self.lable2, self.lable3, self.lable4, self.lable5, self.lable6]
        for label in self.storage:
            label.pack(pady = 2)


    def run(self):
        self.push_button()
        self.root.mainloop()


    def randoma(self):
        a = random.sample(self.storage, 6)
        b = random.sample(self.color_storage, 6)
        for i in range(6):
            a[i].configure(text = b[i], bg = b[i] )

    def up(self):
       for i in range(6):
            self.storage[i].configure(text = self.color_storage[i], bg = self.color_storage[i] )

    def down(self):
        for i in range(6):
            self.storage[i].configure(text = self.color_storage[5 - i], bg = self.color_storage[5 - i] ) 

    def quitt(self):
        choice = messagebox.askyesno("question", "Sure you wanna quit???")
        if choice:
            self.root.destroy()

         


    def push_button(self):

        tk.Button(self.root, text="random", width =12, height = 1, bg = "white", font = ("Arial", 15, "bold") , command = self.randoma).pack(pady = 3)
        tk.Button(self.root, text="up", width =12, height = 1, bg = "white", font = ("Arial", 15, "bold"), command = self.up).pack(pady = 3)
        tk.Button(self.root, text="down", width =12, height = 1, bg = "white", font = ("Arial", 15, "bold"), command = self.down).pack(pady = 3)
        tk.Button(self.root, text="QUIT", width =12, height = 1, bg = "white", font = ("Arial", 15, "bold"), command = self.quitt).place(relx = 0.343, rely = 0.9)
        
      


    def exit(self):
        choise =messagebox.askyesno("quit", "Sure you wanna quit?")
        if choise:
            self.root.destroy()

win = Window("My program", 500, 500, "pink", (True, True))  
win.run()