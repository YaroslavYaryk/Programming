import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from list_of_student import classmates
from random import sample
from tkinter.scrolledtext import ScrolledText

storage = {}

class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.numbers = None
        self.Classmates = {}
        for i,name  in enumerate(classmates,1):
            self.Classmates[i] = name


        self.grab_focus()


    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()
        self.draw_label()
        self.draw_entry()
        self.draw_button()


    def draw_label(self):

        tk.Label(self.root, text = "Enter numbet of iteration",  bg = "#5199FF", fg = "black" ).grid(row = 0, column =0, pady = 10)    

    def draw_entry(self):

        self.numbers = tk.Entry(self.root, width = 30)
        self.numbers.grid(row = 0, column =1)

    def get_number(self):
        list_of_numbers = [int(x) for x in self.numbers.get().split()]
        win = tk.Toplevel(self.root)
        win.geometry("500x500+400+150")
        st = ScrolledText(win, width = 300, height = 100)
        st.pack()
        storage = sample(list_of_numbers, len(list_of_numbers))
        for i in range(len(list_of_numbers)):
            st.insert(tk.END, f"{i+1} - " +  self.Classmates[storage[i]] + "\n")

    def draw_button(self):

        tk.Button(self.root, text = "Get numbers", bg = "#5199FF", fg = "black", bd = 3, command = self.get_number).grid(row = 1, column =1)
