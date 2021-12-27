import tkinter as tk


class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])


        self.label = tk.Label(self.root,text = "Unpressed", bg = "red", font = ("Arial", 15, "bold"), padx = 5, pady = 5)

        self.label.pack()
    def done(self):

        self.label.configure(text = "Pressed", bg = "blue")
        self.butt1["state"] = tk.DISABLED





    def run(self):
        self.push_button()
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

    def push_button(self):

        self.butt1 = tk.Button(self.root, text = "push me",command = self.done, width = 20, height = 2, background = "red",
                            highlightcolor = "blue",font = ("Arial", 10, "bold") )
                            
        self.butt1.place(relx = 0.2, rely = 0.3)


        self.butt2 = tk.Button(self.root, text = "quit",command = self.root.quit, width = 20, height = 2, background = "red",
                            highlightcolor = "blue",font = ("Arial", 10, "bold") )
                            
        self.butt2.place(relx = 0.5, rely = 0.7)


       


win = Window("My program", 500, 500, "green", (True, True))  
win.run()