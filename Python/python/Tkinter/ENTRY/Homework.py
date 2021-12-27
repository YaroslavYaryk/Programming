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
        self.enry = None
        self.lab1 = None
        

    def close_window(self):
        if messagebox.askyesno("Quit","Sure you wanna quit??"):
            self.root.destroy()


    def run(self):
        self.drow_entry()
        self.drow_label()
        self.drow_button()
        self.root.mainloop()

    def get_result(self):
        word = self.enry.get()
        if word:
            sss = eval(word)

            self.lab1.configure(text = "new text ") 
            self.enry.delete(0, tk.END) 
            self.enry.insert( 0 , sss)      

        else:
            lab2 = tk.Label(self.root, text = "you entered nothing", width = 30, height = 2, bg = "purple", fg = "white",
                                            font = ("Arial", 10, "bold"))
            lab2.grid(row = 4, column = 2)


    def delete_all(self):

        self.enry.delete(0, tk.END)





    def drow_label(self):
        self.lab1 = tk.Label(self.root, text = "Your operation", bg = "purple", fg = "yellow", width = 20)    
        self.lab1.grid(row =0, column = 0, sticky = "e")
        return self.lab1

    def drow_entry(self):
        self.enry = tk.Entry(self.root, width = 30, bg = "pink", fg = "blue",
                        highlightbackground = "red", selectforeground = "yellow",
                         selectbackground = "green", justify = "center" )    
        self.enry.grid(row=0, column = 2, sticky = "WE")

        return self.enry

    def drow_button(self):

        butt1 = tk.Button(self.root, width = 20, height =2, text = "get result",command =  self.get_result)
        butt1.grid(row = 2, column = 2)  
        butt1 = tk.Button(self.root, width = 20, height =2, text = "Delete all",command =  self.delete_all)
        butt1.grid(row = 2, column = 3) 
          


some = Window("My App", 500, 500, "purple")
some .run()