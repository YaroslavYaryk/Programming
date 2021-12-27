# import datetime
# d = datetime.datetime.today()

# print(d.strftime("%d-%B-%Y %H:%M:%S"))

import tkinter as tk
from tkinter import messagebox as msg
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window 

my_var=msg.askyesnocancel("Title Here ","Your choice",default='cancel')
# default =  yes or no or cancel
print(my_var) 

my_w.mainloop()