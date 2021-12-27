import tkinter as tk
import child_window as child
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])


    def run(self):
        self.drow_label()
        self.root.mainloop()


    def drow_label(self):
        tk.Label(self.root, text =  "hi there",
                        activebackground = "purple",
                        activeforeground = "white",
                        highlightcolor = "pink",
                        background = "orange",
                        padx = 5,
                        pady = 5,
                        font = ("Arial", 15, "bold")).pack()



    def get_child(self, title , height, width, bg_color , resizable = (False, False)):
        child.ChildWindow(self.root, title, height, width, bg_color, resizable)    


win = Window("My program", 500, 500, "green", (True, True))  
          
win.get_child("Yary", 300,300, "red")
win.run()