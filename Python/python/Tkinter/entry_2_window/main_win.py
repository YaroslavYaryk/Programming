import tkinter as tk
import child_win as child
from tkinter import messagebox
class Window():

    def __init__(self,title, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry("+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.entry1 = None
        self.entry2 = None



    def run(self):
        self.drow_label()
        self.drow_entry()
        self.drow_button()
        self.root.mainloop()


    def check(self):

        # if self.entry1.get() == "Yaryk" and self.entry2.get() == "3103":
        self.get_child("Yary", 500,500, "purple")
           
        # else:
        #     messagebox.showerror("error", "Wrong name or pasword")   
        
    def quit(self):
        choice = messagebox.askyesno("quit", "Sure you wanna quit??")
        if choice:
            self.root.destroy()
        else:
            pass



    def drow_label(self):
        tk.Label(self.root, text =  "Name  ", fg = "yellow", bg = "green",
                        font = ("Arial", 15, "bold")).grid(row =0, column = 1)

        tk.Label(self.root, text =  "Pasword  ", fg = "yellow", bg = "green",
                        font = ("Arial", 15, "bold")).grid(row =1, column = 1)
                        


    def drow_entry(self):

        self.entry1 = tk.Entry(self.root, width = 20)
        self.entry2 = tk.Entry(self.root, width = 20, show = "*")

        self.entry1.grid(row =0, column =2) 
        self.entry2.grid(row = 1, column = 2)

    def drow_button(self):

        tk.Button(self.root, text = "Check", bg = "green", fg = "yellow", command = self.check ).grid(row = 3, column = 1) 
        tk.Button(self.root, text = "Quit", bg = "green", fg = "yellow", command = self.quit ).grid(row = 3, column = 2)                                       




    def get_child(self, title , height, width, bg_color , resizable = (False, False)):
        child.ChildWindow(self.root, title, height, width, bg_color, resizable)    


win = Window("My program", "green", (True, True))  
          
# win.get_child("Yary", 300,300, "red")
win.run()