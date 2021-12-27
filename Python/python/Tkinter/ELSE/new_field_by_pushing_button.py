import tkinter as tk
win = tk.Tk()
win.title("My GIU")
win.geometry("500x500+500+150")
win.config(bg = "purple")

counter1 = 0
counter2 = 0
counter3 = 0
new_win = None

def label1():
    global counter3
    if counter3%2 == 0:

        label1 = tk.Label(new_win,text = "hey",
                                activebackground = "purple",
                                activeforeground = "white",
                                highlightcolor = "pink",
                                background = "orange",
                                padx = 5,
                                pady = 5,
                                font = ("Arial", 15, "bold")).pack(padx = 10, pady = 10)
    else:
        pass
    counter3+=1                            


def main(title, width, height, color,x,y):
    
    global new_win
    new_win = tk.Toplevel(win)
    new_win.config(bg = color)
    new_win.title(title)
    new_win.geometry(f"{width}x{height}+{x}+{y}")
    new_win.wm_attributes("-topmost", 1)

    return new_win

def first():
    global counter1 
    if counter1 == 0:
        main("My New1", 200,200, "red",650,300)
        b1 = tk.Button(new_win,text = "hello",
                                command = label1,
                                activeforeground = "red",
                                activebackground = "blue",
                                padx = 5,
                                pady = 5,
                                background = "green",
                                bd = 2,
                                highlightcolor = "white",
                                font = ("Arial", 10, "bold") )

        b1.pack()
    else:
        pass
    counter1+=1


def second():
    global counter2
    if counter2 == 0:
        main("My New2", 300, 300, "blue", 600,250)
    else:
        pass
    counter2+=1


btn1 = tk.Button(win, text = "open first field",
                        command = first,
                        activeforeground = "red",
                        activebackground = "green",
                        padx = 5,
                        pady = 5,
                        background = "red",
                        bd = 5,
                        highlightcolor = "white",
                        font = ("Arial", 10, "bold"),
                         )
btn1.place(x=10, y=450)

btn2 = tk.Button(win,  text = "open first field",
                        command = second,
                        activeforeground = "red",
                        activebackground = "green",
                        padx = 5,
                        pady = 5,
                        background = "red",
                        bd = 5,
                        highlightcolor = "white",
                        font = ("Arial", 10, "bold"),
                        justify = "left",)
btn2.place(x=100, y=10)



# btn1.pack()
win.mainloop()