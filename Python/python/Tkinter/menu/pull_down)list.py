import tkinter as tk
class Window():

    def __init__(self,title, height, width, bg_color, resizable = (False, False)):

        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+150")
        self.root.config(bg = bg_color)
        self.root.resizable = (resizable[0], resizable[1])
        self.save_auto = tk.BooleanVar()

    def run(self):
        self.draw_menu()
        self.root.mainloop()

    def check_checkbox(self):

        if self.save_auto.get == 1:
            self.save_auto = tk.BooleanVar(value = 1)
            
        return self.save_auto

    def draw_menu(self):

        menu_bar = tk.Menu(self.root)
        
        
        new_menu = tk.Menu(menu_bar, tearoff = 0, bg = "blue", activebackground = "blue", activeforeground = "yellow")
        new_menu2 = tk.Menu(menu_bar, tearoff = 0)
        new_save = tk.Menu(new_menu, tearoff = 0)

        

        new_menu.add_command(label = "Open file")
        new_menu.add_command(label = "Open Folder")
        new_menu.add_command(label = "Open workspace")
        new_menu.add_separator()

        new_menu.add_command(label = "Save")
        new_menu.add_cascade(label = "Save as", menu = new_save)


        
        new_menu2.add_command(label = "Cut")
        new_menu2.add_command(label = "Copy")
        new_menu2.add_command(label = "Paste")
        new_menu2.add_separator()
        new_menu2.add_checkbutton(label = "auto save", onvalue = 1, offvalue = 0, variable = self.save_auto)


        new_save.add_command(label = "new")
        new_save.add_command(label = "Brand new")
        new_save.add_command(label = "old")


        menu_bar.add_cascade(label = "File", menu = new_menu)
        menu_bar.add_cascade(label = "Edit", menu = new_menu2)


        self.root.configure(menu = menu_bar)     


win = Window("My menu", 300,400, "#5199FF")
win.run()        