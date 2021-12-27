import tkinter as tk
import string
from tkinter import messagebox
class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.entry = tk.Entry(self.root, width = 20)
        self.lab1 = None
        self.grab_focus()
        self.drow_label()
        self.drow_button()
        self.entry.grid(row = 0, column = 1)


    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()


    def run(self):
        self.drow_label()
        self.drow_button()
        self.root.mainloop()

    def get_shifr(self):
        word = self.entry.get()
        if word:
            key = 3
            sss = ''
            a = string.ascii_lowercase
            alphabet = a * 2
            for i in word:
                position = a.find(i)
                new_position = position + key
                if i in alphabet:
                    sss += alphabet[new_position]
                else:
                    sss += i

            self.lab1.configure(text = "new text ") 
            self.entry.delete(0, tk.END) 
            self.entry.insert( 0 , sss)      

        else:
            lab2 = tk.Label(self.root, text = "you entered nothing", width = 30, height = 2, bg = "purple", fg = "white",
                                            font = ("Arial", 10, "bold"))
            lab2.grid(row = 4, column = 2)


    def delete_all(self):

        self.entry.delete(0, tk.END)

    def quit(self):
        choice = messagebox.askyesno("quit", "Sure you wanna quit??")
        if choice:
            self.root.destroy()
        else:
            pass    


    def drow_label(self):
        self.lab1 = tk.Label(self.root, text = "Your text", bg = "purple", fg = "yellow", width = 20)    
        self.lab1.grid(row =0, column = 0)
        return self.lab1



    def drow_button(self):

        butt1 = tk.Button(self.root, width = 20, height =1, text = "Push me", command = self.get_shifr)
        butt1.grid(row = 2, column = 1)  
        butt1 = tk.Button(self.root, width = 20, height =1, text = "Delete all", command = self.delete_all)
        butt1.grid(row = 2, column = 2)
        butt1 = tk.Button(self.root, width = 20, height =1, text = "quit", command = self.quit)
        butt1.grid(row = 2, column = 0)                     


