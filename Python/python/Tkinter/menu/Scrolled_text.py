import tkinter as tk
from tkinter.scrolledtext import ScrolledText
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
        self.draw_scrolled_text()

        self.root.mainloop()

    def check_checkbox(self):

        if self.save_auto.get == 1:
            self.save_auto = tk.BooleanVar(value = 1)
            
        return self.save_auto


    def draw_scrolled_text(self):
        self.st = ScrolledText(self.root, selectforeground = "white", fg = "black", font = ("Consolas", 11),
                            wrap = "word", width = 200, height = 100)
        self.st.pack()    

    def draw_menu(self):

        menu_bar = tk.Menu(self.root)
        
        
        new_menu = tk.Menu(menu_bar, tearoff = 0)
        new_menu2 = tk.Menu(menu_bar, tearoff = 0)

        
        new_menu.add_command(label = "New")
        new_menu.add_command(label = "New Window", command = self.new_win)
        new_menu.add_command(label = "Open ")

        new_menu.add_separator()

        new_menu.add_command(label = "Save")
        new_menu.add_cascade(label = "Save as")


        
        new_menu2.add_command(label = "Cut")
        new_menu2.add_command(label = "Copy")
        new_menu2.add_command(label = "Paste")
        new_menu2.add_separator()
        new_menu2.add_checkbutton(label = "auto save", onvalue = 1, offvalue = 0, variable = self.save_auto)



        menu_bar.add_cascade(label = "File", menu = new_menu)
        menu_bar.add_cascade(label = "Edit", menu = new_menu2)


        self.root.configure(menu = menu_bar)     


win = Window("Notepad", 500,900, "#5199FF")
win.run()        