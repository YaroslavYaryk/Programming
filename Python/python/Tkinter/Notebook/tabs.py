import tkinter as tk
from tkinter.ttk import Notebook
from list_of_student import classmates
from random import sample
from tkinter.scrolledtext import ScrolledText
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.main_tab = Notebook(self.root)
        self.tab1 = tk.Frame(self.main_tab)
        self.tab2 = tk.Frame(self.main_tab)
        self.main_tab.add(self.tab1, text = "first")
        self.main_tab.add(self.tab2, text = "second")
        self.main_tab.pack( fill = tk.BOTH)
        self.main_tab.enable_traversal
        self.from_entry = None
        self.to_entry = None
        self.how_many_entry = None
        self.Classmates = {}
        for i,name  in enumerate(classmates,1):
            self.Classmates[i] = name
        

    def run(self):
        self.get_first_tab()
        self.get_second_tab()
        self.root.mainloop()
  

    def get_first_tab(self):
        self.draw_label("first")
        self.draw_entry("first")
        self.draw_button("first")
   
   
    def get_second_tab(self):
        self.draw_entry("second")
        self.draw_button("second")


    def draw_label(self, name_type):
        if name_type == "first":
            tk.Label(self.tab1, text = "Enter numbet of iteration",  bg = "#5199FF", fg = "black" ).pack()   
            

    def draw_entry(self, name_type):
        if name_type == "first":
            self.numbers = tk.Entry(self.tab1, width = 30)
            self.numbers.pack()
        elif name_type == "second":
            self.from_entry = tk.Entry(self.tab2)
            self.from_entry.pack()
            self.to_entry = tk.Entry(self.tab2)
            self.to_entry.pack()
            self.how_many_entry = tk.Entry(self.tab2)
            self.how_many_entry.pack()


    def get_number(self, name_type):
        if name_type == "first":
            list_of_numbers = [int(x) for x in self.numbers.get().split()]
            win = tk.Toplevel(self.tab1)
            win.geometry("500x500+400+150")
            st = ScrolledText(win, width = 300, height = 100)
            st.pack()
            storage = sample(list_of_numbers, len(list_of_numbers))
            for i in range(len(list_of_numbers)):
                st.insert(tk.END, f"{i+1} - " +  self.Classmates[storage[i]] + "\n")
        elif name_type == "second":
            from_ent = int(self.from_entry.get())
            to_ent = int(self.to_entry.get())
            how_many_ent = int(self.how_many_entry.get())
            storage = sample(range(from_ent, to_ent+1), how_many_ent)
            win = tk.Toplevel(self.tab2)
            win.geometry("500x500+400+150")
            st = ScrolledText(win, width = 300, height = 100)
            st.pack()
            for i in range(len(self.Classmates)):
                st.insert(tk.END, f"{i+1} - " +  self.Classmates[storage[i]] + "\n")


    def draw_button(self, name_type):
        if name_type == "first":
            tk.Button(self.tab1, text = "Get numbers", bg = "#5199FF", fg = "black", bd = 3, command = lambda:self.get_number("first")).pack()
        elif name_type == "second":
            tk.Button(self.tab2, text = "Get numbers", bg = "#5199FF", fg = "black", bd = 3, command = lambda:self.get_number("second")).pack()


obj = Window("Notebook", 110, 300, "pink")
obj.run()