import tkinter as tk


class Window():

    def __init__(self,title, height, width, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = "blue")
        self.root.resizable = (resizable[0], resizable[1])


    def run(self):
        self.draw_menu()
        self.root.mainloop()


    def draw_menu(self):

        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label = "File")
        menu_bar.add_command(label = "Edit")
        menu_bar.add_command(label = "Selection")
        menu_bar.add_command(label = "View")
        menu_bar.add_command(label = "Go")
        menu_bar.add_command(label = "Run")
        menu_bar.add_command(label = "Terminal")
        menu_bar.add_command(label = "Help")
        


        self.root.configure(menu = menu_bar)     


win = Window("My menu", 300,400)
win.run()        