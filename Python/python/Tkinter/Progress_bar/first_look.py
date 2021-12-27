import tkinter as tk
from tkinter.ttk import Progressbar
from time import sleep
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.status = None


    def run(self):
        self.drow_status_bar()
        self.draw_button()
        self.root.mainloop()

    def drow_status_bar(self):
        self.status = Progressbar(self.root, orient = tk.HORIZONTAL, mode = "determinate", length = 300)
        self.status.pack(pady = 20)

    def start_progressbar(self):
        for i in range(101):
            sleep(0.05)
            self.status.configure(value = i)
            self.status.update()

    def draw_button(self):
        butt1 = tk.Button(self.root, text = "start", command = self.start_progressbar)
        butt1.pack(pady = 20)

obj = Window("status bar", 500, 500, "#E5F0FF")
obj.run()