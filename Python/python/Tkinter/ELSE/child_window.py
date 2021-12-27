import tkinter as tk


class ChildWindow():

    def __init__(self,parent,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.grab_focus()
        self.drow_label()
        self.drow_button()


    def grab_focus(self):

        self.root.focus_set()
        self.root.grab_set()


    def drow_label(self):    

        tk.Label(self.root, text = "hello",
                        activebackground = "purple",
                        activeforeground = "white",
                        highlightcolor = "pink",
                        background = "orange",
                        padx = 5,
                        pady = 5,
                        font = ("Arial", 15, "bold")).pack()

    def drow_button(self):

        tk.Button(self.root, text = "Push ",
                            highlightcolor = "blue",
                            highlightbackground = "black",
                            activebackground = "orange",
                            activeforeground = "pink",
                            font = ("Arial", 20, "bold"),
                            fg = "red",
                            bg = "brown",
                            padx = 5,
                            pady = 5,
                            relief = tk.RAISED,
                            bd = 10).place(x = 90, y = 90)                    


