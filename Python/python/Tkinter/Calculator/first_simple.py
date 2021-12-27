import tkinter as tk
from tkinter import messagebox
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.root.protocol("WM_DELETE_WINDOW", self.close_window)
        self.storage = 0
 
        self.enry = None

        
        

    def close_window(self):
        if messagebox.askyesno("Quit","Sure you wanna quit??"):
            self.root.destroy()


    def run(self):
        self.drow_entry()
        self.drow_button()
        self.root.mainloop()

    def get_result(self):
        
        self.enry.delete(0, tk.END) 
        self.enry.insert( 0 , self.storage)
        self.storage = 0      


    def pluss(self):

        self.storage += int(self.enry.get())
        self.enry.delete(0, tk.END)
        print(self.storage)
        return self.storage


    def minus(self):
        self.storage += int(self.enry.get())
        if self.storage == 0:
            messagebox.showwarning("warning", f"0-{int(self.enry.get())}")
        else:
            self.storage -= int(self.enry.get())

        self.enry.delete(0, tk.END)
        print(self.storage)
        return self.storage        


    def product(self):

        self.storage *= int(self.enry.get())
        self.enry.delete(0, tk.END)

        return self.storage


    def divide(self):
        if self.storage == 0:
            messagebox.showerror("error", "Division by zero")
            self.storage = 0
        else:
            self.storage /= int(self.enry.get())



    def delete_all(self):

        self.enry.delete(0, tk.END)
    
    def dell(self):

        self.enry.delete(len(self.enry.get()) - 1, tk.END)

    def insert_num(self, num):
        self.enry.insert(tk.END, num)


    def drow_entry(self):
        self.enry = tk.Entry(self.root, width = 30, bg = "pink", fg = "blue",
                        highlightbackground = "red", selectforeground = "yellow",
                         selectbackground = "green", justify = "center", font = ("Arial", 14, "bold") )    
        self.enry.pack(ipady = 5)
        tk.Label( self.root, bg = "purple").pack()

        return self.enry 

    def drow_button(self):
        self.bottom_frame = tk.Frame(self.root)
        self.top_frame = tk.Frame(self.root)
        self.left_frame = tk.Frame(self.root)
        self.right_frame = tk.Frame(self.root)


        self.bottom_frame.pack(padx = 1, pady = 1)
        self.left_frame.pack(padx = 1,pady = 1)
        self.top_frame.pack(padx = 1,pady = 1)
        self.right_frame.pack(padx = 1,pady = 1)

    

        tk.Button(self.bottom_frame, text = "1", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("1")).pack(side = "left", padx = 1)
        tk.Button(self.bottom_frame, text = "2", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("2")).pack(side = "left", padx = 1)
        tk.Button(self.bottom_frame, text = "3", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("3")).pack(side = "left", padx = 1)
        tk.Button(self.left_frame, text = "4", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("4")).pack(side = "left", padx = 1)
        tk.Button(self.left_frame, text = "5", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("5")).pack(side = "left", padx = 1)
        tk.Button(self.left_frame, text = "6", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("6")).pack(side = "left", padx = 1)
        tk.Button(self.top_frame, text = "7", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("7")).pack(side = "left", padx = 1)
        tk.Button(self.top_frame, text = "8", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("8")).pack(side = "left", padx = 1)
        tk.Button(self.top_frame, text = "9", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("9")).pack(side = "left", padx = 1)
        tk.Button(self.right_frame, text = "e", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("e")).pack(side = "left", padx = 1)
        tk.Button(self.right_frame, text = "0", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num("0")).pack(side = "left", padx = 1)
        tk.Button(self.bottom_frame, text = "+", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  self.pluss).pack(side = "left", padx = 1)
        tk.Button(self.left_frame, text = "-", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  self.minus).pack(side = "left", padx = 1)
        tk.Button(self.top_frame, text = "*", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  self.product).pack(side = "left", padx = 1)
        tk.Button(self.right_frame, text = "/", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  self.divide).pack(side = "left", padx = 1)
        tk.Button(self.right_frame, text = ".", bg = "green", font = ("Arial", 15, "bold"),  width = 10, height = 2,command =  lambda:  self.insert_num(".")).pack(side = "left", padx = 1)

        tk.Button(self.root, text = "Get result",width = 20, bg = "red", fg = "blue", font = ("Arial", 15, "bold"), height = 1, bd = 5, command = self.get_result).pack(anchor = "s")
        tk.Button(self.root, text = "Del last", width = 20, bg = "red", fg = "blue", font = ("Arial", 15, "bold"), height = 1, bd = 5, command = self.dell).pack(anchor = "s")
        tk.Button(self.root, text = "Dell all", width = 20, bg = "red", fg = "blue", font = ("Arial", 15, "bold"), height = 1, bd = 5, command = self.delete_all).pack(anchor = "s")

 
        
some = Window("My App", 500, 500, "purple")
some .run()