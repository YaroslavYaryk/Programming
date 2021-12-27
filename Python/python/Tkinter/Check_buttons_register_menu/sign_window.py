import tkinter as tk
import register_window as child_reg
from tkinter import messagebox
import sqlite3 as sq


db =  sq.connect("storage_table.db")
cur = db.cursor()

class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.storage = child_reg.storage
        self.user_name = None
        self.password = None
        self.grab_focus()
        self.drow_label()
        self.drow_entry()
        self.drow_button()


    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()

    
    def sign_in(self):
        # cur.execute("INSERT INTO storage VALUES ('111', '111', '111')")       
        cur.execute(f"SELECT * FROM storage WHERE name = '{self.user_name.get()}'")
        result = cur.fetchall()
        print(result)
        if cur.fetchall() is None:
            messagebox.showwarning("Warning", "you must sign up first")
            self.root.destroy()
        elif result[0][0] == self.user_name.get() and result[0][2] == self.password.get():
            messagebox.showinfo("Info", "Access is allowed") 
            self.root.destroy() 
           
        else:
            print(result[0][0] == self.user_name.get(), result[0][2] == self.password.get())
            messagebox.showerror("Error", "Password or name is not appropriate")
            self.password.delete(0, tk.END)   


    def drow_label(self):    

        tk.Label(self.root, text = "User name", bg ="#5199FF", pady = 20, 
                        font = ("Arial", 12, "bold")).grid(row = 0, column = 0)
        

        tk.Label(self.root, text = "Password", bg ="#5199FF", pady = 20, 
                        font = ("Arial", 12, "bold")).grid(row = 1, column = 0)
        


    def drow_entry(self):
        self.user_name = tk.Entry(self.root, width  = 30, background ="#4A69FF",font = ("Arial", 12, "bold") )
        self.user_name.grid(row = 0, column = 1, columnspan = 3, pady = 10)
        self.password = tk.Entry(self.root, width  = 30, background ="#4A69FF", show = "*" ,font = ("Arial", 12, "bold"))
        self.password.grid(row = 1, column = 1, columnspan = 3, pady = 10)   



    def drow_button(self):

        tk.Button(self.root, text = "Save all ", command = self.sign_in,
                           bg = "#00848C", width = 20, height = 2).grid(row = 3, column = 1)
                                              

