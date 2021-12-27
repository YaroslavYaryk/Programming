import tkinter as tk

count = 0

def say_pidar():
    global count
    if count%2==0:

        label = tk.Label(text = "pidar",
                        bg = "purple",
                        fg = "yellow",
                        font = ("Arial", 20, "bold"))
        btn1["text"] = "hi pidar"
        label.pack()
    else:
        label2 = tk.Label(text = "mudila",
                        bg = "black",
                        fg = "blue",
                        font = ("Arial", 20, "bold"))
        btn1["text"] = "hi mudila"
        label2.pack()    
    count += 1

win = tk.Tk()
win.geometry("500x500+500+150")
win.title("Yaryk")
win.config(bg = "Green")
btn1 = tk.Button(text = "Push",
                 command = say_pidar,
                 highlightcolor = "blue",
                 highlightbackground = "black",
                 activebackground = "orange",
                 activeforeground = "pink",
                 font = ("Arial", 20, "bold"),
                 fg = "red",
                 bg = "brown",

                 width = 10,
                 height = 1,
                 
                 relief = tk.RAISED,
                 bd = 10)

btn1.place(relx = 0.32, rely = 0.4)                 

win.mainloop()