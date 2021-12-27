import tkinter as tk
from tkinter import messagebox
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+270")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.storage = 0
 
        self.enry = None
        self.root.bind("<Key>", self.press_key)
        
        

    def close_window(self):
        if messagebox.askyesno("Quit","Sure you wanna quit??"):
            self.root.destroy()


    def run(self):
        self.drow_entry()
        self.drow_button()
        self.root.mainloop()

   
    def drow_entry(self):
        self.enry = tk.Entry(self.root,  justify = "right" , font = ("Arial", 15), width = 15)
        self.enry.insert(0,"0")    
        self.enry.grid(row = 0, column = 0, columnspan =4, sticky = "we", padx = 5, ipady = 5)

        return self.enry 

    def press_key(self, event):
        if event.char.isdigit():
            self.add_digit(event.char)
        elif event.char in "+-*/":
            self.add_operation(event.char) 
        elif event.char == "\r":
            self.get_result()       


    def add_digit(self, num):
        value = self.enry.get()
        try:
            if value[0] == "0" and len(value) == 1 :
                self.enry.delete(0,1)
        except IndexError:
            self.enry.delete(0, tk.END)
            self.enry.insert(0, "0")
                    
        self.enry.insert(tk.END, num)


    def add_operation(self, operation):
        value = self.enry.get()
        if value[len(value) - 1] in "+-/*":
            self.enry.delete(len(value) -1, tk.END)
        elif "+" in value or "-" in value or "*" in value or "/" in value:
            self.get_result()
            value = self.enry.get()
        self.enry.insert(tk.END, operation)


    def dell(self, word):
        if len(self.enry.get()) == 0:
            self.enry.insert(0, "0")
        else:
            if word == "all":
                self.enry.delete(0, tk.END)
                self.enry.insert(0, "0")
            elif word == "one":
                self.enry.delete(len(self.enry.get())-1, tk.END)          


    def put_butt(self, num):
        return tk.Button(self.root, text = num, bd = 5, fg = "#0043A4" ,font = ("Arial", 17), bg = "#F2F8FD", command = lambda : self.add_digit(num))

    def put_operation(self, operation):
        return tk.Button(self.root, bg = "#58595B",text = operation, bd = 5 ,font = ("Arial", 13),\
            fg = "white",  command = lambda : self.add_operation(operation))
        

    def put_equal(self, operation):
        return tk.Button(self.root, text = operation, bd = 5, bg = "#7AB1FF" ,font = ("Arial", 13),\
            fg = "red",  command = self.get_result)        

    def put_delete_all(self):
        return tk.Button(self.root, text = "C", bd = 5, bg = "#F85C50",  font = ("Arial", 13),\
            fg = "white",  command =  lambda : self.dell("all")) 

    def put_delete_one(self):
        return tk.Button(self.root, text = "<-", bd = 5, bg = "#FF756B" ,font = ("Arial", 13),\
            fg = "white",  command =  lambda : self.dell("one"))

    def get_point(self):
        value = self.enry.get()
        if value[-1] != ".":
            self.enry.insert(len(value), ".")        

    def put_point(self):
        return tk.Button(self.root, text = ".", bd = 5, font = ("Arial", 15), command = self.get_point)

    def get_result(self):

        value = self.enry.get()
        if value[-1] in "+-/*":
            operation = value[-1]
            value = value[:-1] + operation + value[:-1]
        if value[-1] == "%":
            self.enry.delete(len(self.enry.get())-1, tk.END)
            value = float(self.enry.get())/100    
        self.enry.delete(0, tk.END)
        try:
            self.enry.insert(0, eval(str(value)))
        except (NameError, SyntaxError):
            messagebox.showerror("Error", "You must entered someth else")    
            self.enry.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showwarning("Warning", "Division by zero")    
            self.enry.insert(0, 0)

            
    def drow_button(self):
       
        self.put_butt("1").grid(row = 4, column = 0, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("2").grid(row = 4, column = 1, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("3").grid(row = 4, column = 2, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("4").grid(row = 3, column = 0, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("5").grid(row = 3, column = 1, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("6").grid(row = 3, column = 2, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("7").grid(row = 2, column = 0, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("8").grid(row = 2, column = 1, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("9").grid(row = 2, column = 2, sticky = "nswe", padx = 5, pady = 5)
        self.put_butt("0").grid(row = 5, column = 1, sticky = "nswe", padx = 5, pady = 5)
        self.put_operation("+").grid(row = 4, column = 3, sticky = "nswe", padx = 5, pady = 5)
        self.put_point().grid(row = 5, column = 2, sticky = "nswe", padx = 5, pady = 5)

        self.put_operation("-").grid(row = 3, column = 3, sticky = "nswe", padx = 5, pady = 5)
        self.put_operation("*").grid(row = 2, column = 3, sticky = "nswe", padx = 5, pady = 5)
        self.put_operation("/").grid(row = 1, column = 3, sticky = "nswe", padx = 5, pady = 5)
        self.put_operation("%").grid(row = 1, column = 2, sticky = "nswe", padx = 5, pady = 5)
        self.put_operation("e").grid(row = 5, column = 0, sticky = "nswe", padx = 5, pady = 5)

        self.put_equal("=").grid(row = 5, column = 3, sticky = "nswe", padx = 5, pady = 5)
        
        self.put_delete_all().grid(row = 1, column = 0, sticky = "nswe", padx = 5, pady = 5)
        self.put_delete_one().grid(row = 1, column = 1, sticky = "nswe", padx = 5, pady = 5)
        self.root.grid_columnconfigure(0,minsize = 60)
        self.root.grid_columnconfigure(1,minsize = 60)
        self.root.grid_columnconfigure(2,minsize = 60)
        self.root.grid_columnconfigure(3,minsize = 57)
        self.root.grid_columnconfigure(4,minsize = 57)


        self.root.rowconfigure(1, minsize = 60)
        self.root.rowconfigure(2, minsize = 60)
        self.root.rowconfigure(3, minsize = 60)
        self.root.rowconfigure(4, minsize = 60)
        self.root.rowconfigure(5, minsize = 60)


some = Window("Calculator", 350, 240, "#E5F0FF")
some .run()