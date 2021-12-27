import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3 as sq

storage = {}


db =  sq.connect("storage_table.db")
cur = db.cursor()

"""cur.execute() help us to make some operation  """

# cur.execute("DROP TABLE IF EXISTS storage") # delete table if it exists

##create table if it not exists: name = users , and other fieds below
##user_id = it's like a counter that increments when we create new row 
cur.execute("""CREATE TABLE IF NOT EXISTS storage( 
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
)""")


class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.gender = tk.StringVar()
        self.confirm_all = tk.StringVar(value = "No")
        self.storage = {}
        self.registered = []
        self.user_names = []
        self.val = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.entry_name = None
        self.entry_user_name = None
        self.entry_mail = None
        self.password = None
        self.confirm_password = None
        self.day = None
        self.month = None
        self.year = None
        self.name = None


        self.grab_focus()
        self.drow_label()
        self.drow_entry()
        self.drow_radiobutton()
        self.drow_checkbutton()
        self.drow_button()
        self.drow_combobox()

    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()

    def is_empty(self, entry):

        return len(entry.get()) != 0

    def dell_word(self, word):
        if word == "All":
            store = [self.entry_name, self.entry_user_name, self.entry_mail, self.password, self.confirm_password]
            for elem in store:
                elem.delete(0, tk.END)
        else:
            word.delete(0, tk.END)        


    def enter_name(self):
        global storage
        if self.is_empty(self.entry_name):
            value = self.entry_name.get()
            self.name = self.entry_name.get()
        else:
            messagebox.showwarning("Warning", "Name is empty")
        return self.name    
                    

    def enter_user(self):
        if self.is_empty(self.entry_user_name):
            value = self.entry_user_name.get()
            if value in self.user_names:
                messagebox.showinfo("info", "this user name is not avaluble,\
                                            try to figure out smth else!!!")
            else:
                self.user_name = self.entry_user_name.get()
        else:
            messagebox.showwarning("Warning", "User_name is empty")  
        return self.user_name        

    def enter_mail(self):
        global storage
        value = self.entry_mail.get()
        if self.is_empty(self.entry_mail):
            if value in self.registered:
                 messagebox.showinfo("info", "this mail is already taken\
                                        thy to figure smth else")
            else:
                self.mail = self.entry_mail.get()
        else:
            messagebox.showwarning("Warning", "Mail is empty")      
        return storage


    def enter_password(self):
        global storage
        if self.is_empty(self.password) and self.is_empty(self.confirm_password):

            value1  = self.password.get()
            value2  = self.confirm_password.get()
            if len(value1) < 8:
                messagebox.showwarning("Warning", "lenth of password must be longer")
            elif value1 != value2: 
                messagebox.showerror("Error", "Passwords are not equal")
                self.dell_word(self.password)
                self.dell_word(self.confirm_password)
            else:
                self.password = value1  
            return self.password

    def chose_gender(self):
        global storage

        storage["gender"] = self.gender.get()
        return storage

    def confirm_age_and_all(self, word):
        global storage

        if word == "everything":
            if self.confirm_all.get() == "No":
                messagebox.showwarning("Warning", "you forgot to confirm all conditions!!!")
                self.dell_word("all")
        return storage
                
    def save_all(self):
        self.enter_name()
        self.enter_user()
        self.enter_mail()
        self.chose_gender()
        self.enter_password()
        self.confirm_age_and_all("everything")
        if len(storage) == 6:
            messagebox.showinfo("Info", "Everything is saved")
        self.root.destroy()  
        
        cur.execute(f"SELECT name FROM storage WHERE name = '{self.user_name}'")
        if cur.fetchone() is None:
            cur.execute("INSERT INTO storage VALUES(?,?,?)", (self.user_name, self.mail,self.password) )
            db.commit()
        else:
            print(f"Login {self.user_name} already exists")    
            
        
    def template_entry(self):

        return tk.Entry(self.root, width  = 40, background ="#4A69FF" , justify = "left")    

    def drow_entry(self):

       self.entry_name = self.template_entry()
       self.entry_name.grid(row = 0, column = 1, columnspan = 3, pady = 10)
       self.entry_user_name = self.template_entry()
       self.entry_user_name.grid(row = 1, column = 1, columnspan = 3, pady = 10)
       self.entry_mail = self.template_entry()
       self.entry_mail.grid(row = 2, column = 1, columnspan = 3, pady = 10)
       self.password = tk.Entry(self.root, width  = 40, background ="#4A69FF", show = "*" )
       self.password.grid(row = 5, column = 1, columnspan = 3, pady = 10)
       self.confirm_password = tk.Entry(self.root, width  = 40, background ="#4A69FF", show = "*" )
       self.confirm_password.grid(row = 6, column = 1, columnspan = 3, pady = 10)

    def template_label(self, text):
        return tk.Label(self.root, text = text,
                        bg = "#5199FF",
                        font = ("Arial", 10, "bold"), justify = "left")


    def drow_label(self):    

        self.template_label("Your name").grid(row = 0, column = 0, pady = 10, sticky ="w") 
        self.template_label("Your user name").grid(row = 1, column = 0, pady = 10, sticky ="w")  
        self.template_label("Your mail").grid(row = 2, column = 0, pady = 10, sticky ="w")   
        self.template_label("Your gender").grid(row = 3, column = 0, pady = 10, sticky ="w") 
        self.template_label("Password").grid(row = 5, column = 0, pady = 10, sticky ="w")
        self.template_label("Confirm pasword").grid(row = 6, column = 0, pady = 10, sticky ="w")
        self.template_label("Date of birth").grid(row = 4, column = 0, pady = 10, sticky ="w")  


    def drow_combobox(self): 

        self.day = Combobox(self.root, values = list(range(1,32)), state = "readonly", width = -5)
        self.day.grid(row = 4, column = 1, sticky = "we")
        self.month = Combobox(self.root, values = self.val, state = "readonly", width = -5)
        self.month.grid(row = 4, column = 2, sticky = "we")
        self.year = Combobox(self.root, values = list(range(2020,1900,-1)), state = "readonly", width = -5)
        self.year.grid(row = 4, column = 3, sticky = "we")


    def drow_radiobutton(self):

        self.male = tk.Radiobutton(self.root, text = "Male", selectcolor = "yellow",
                                  variable = self.gender, value = "Male", bg = "#5199FF",
                                   activebackground = "#0043A4",font = ("Arial", 10, "bold"))

        self.female = tk.Radiobutton(self.root, text = "Female", selectcolor = "yellow",
                                  variable = self.gender, value = "Female", bg = "#5199FF",
                                   activebackground = "#0043A4", font = ("Arial", 10, "bold"))

        self.male.grid(row = 3 , column = 1)    
        self.female.grid(row = 3 , column = 2)                          


    def drow_checkbutton(self):

        self.confirm_everything = tk.Checkbutton(self.root, variable = self.confirm_all, offvalue = "No", onvalue = "Yes",
                                        bg = "#5199FF", text = "Confirm all conditions" , selectcolor = "#7AB1FF", font = ("Arial", 10, "bold"),
                                        activebackground = "#052555")
        self.confirm_everything.grid(row = 7, column = 0)
        


    def drow_button(self):

        tk.Button(self.root, text = "Save all ",
                           bg = "#00848C", width = 20, height = 2, command = self.save_all).grid(row = 8, column = 0)                    

    def return_storage(self):
        return self.storage

# db.close()