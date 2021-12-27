import tkinter as tk
import chosen_elements as child_reg
from tkinter import messagebox
from list_of_student import classmates
from random import sample
from tkinter.scrolledtext import ScrolledText

class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.from_entry = None
        self.to_entry = None
        self.how_many_entry = None

        self.Classmates = {}
        for i,name  in enumerate(classmates,1):
            self.Classmates[i] = name
        self.grab_focus()
        self.draw_label()
        self.draw_entry()
        self.draw_button()




    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()

    def draw_label(self):

        tk.Label(self.root, text = "From", bg = "#5199FF", fg = "black").grid(row = 0, column = 0, pady = 15)
        tk.Label(self.root, text = "To", bg = "#5199FF", fg = "black").grid(row = 1, column = 0, pady = 15)
        tk.Label(self.root, text = "How many", bg = "#5199FF", fg = "black").grid(row = 2, column = 0, pady = 15)


    def draw_entry(self):
        
        self.from_entry = tk.Entry(self.root)
        self.from_entry.grid(row = 0, column = 1, pady = 15)
        self.to_entry = tk.Entry(self.root)
        self.to_entry.grid(row = 1, column = 1, pady = 15)
        self.how_many_entry = tk.Entry(self.root)
        self.how_many_entry.grid(row = 2, column = 1, pady = 15)



    def get_number(self):
        from_ent = int(self.from_entry.get())
        to_ent = int(self.to_entry.get())
        how_many_ent = int(self.how_many_entry.get())
        storage = sample(range(from_ent, to_ent+1), how_many_ent)
        win = tk.Toplevel(self.root)
        win.geometry("500x500+400+150")
        st = ScrolledText(win, width = 300, height = 100)
        st.pack()
        for i in range(len(self.Classmates)):
            st.insert(tk.END, f"{i+1} - " +  self.Classmates[storage[i]] + "\n")



    def draw_button(self):

        tk.Button(self.root, text = "Get numbers", bg = "#5199FF", fg = "black", bd = 3, command = self.get_number).grid(row = 3, column =1)
    

    


