import tkinter as tk
from tkinter import messagebox


class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])



    def run(self):
        self.push_button()

        self.root.mainloop()


    

    def push_button(self):

        tk.Button(self.root, text="info", width = 20, height = 2, command = lambda: messagebox.showinfo("info", "info message")).pack()
        tk.Button(self.root, text="warning", width = 20, height = 2, command = lambda: messagebox.showwarning("warning", "warning message")).pack()
        tk.Button(self.root, text="error", width = 20, height = 2, command = lambda: messagebox.showerror("error", "error message")).pack()
        tk.Button(self.root, text="close", command = self.exit, width = 20, height = 2).pack(side = "bottom")


    def exit(self):
        choise =messagebox.askyesno("quit", "Sure you wanna quit?")
        if choise:
            self.root.destroy()

win = Window("My program", 500, 500, "green", (True, True))  
win.run()