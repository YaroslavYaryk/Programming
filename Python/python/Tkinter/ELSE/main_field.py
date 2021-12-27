import tkinter as tk

count = 0
count2 = 0


def disable_all():
    global count2
    
    if count2&2==0:
        b1["state"] = tk.DISABLED
        btn3["state"] = tk.DISABLED
        btn2["text"] = "status: Disabled"
        
    else:
        b1["state"] = tk.NORMAL
        btn3["state"] = tk.NORMAL
        btn2["text"] = "status: Normal"
    count2+=2
        
           
def counter():
    global count
    count+=1
    b1["text"] = f"you've pressed {count}"  

win = tk.Tk()
win.title("My GUI")
win.geometry("500x500+500+150")
win.resizable(False,False)
win.config(bg = "blue")
b1 = tk.Button(win, text = f"you've pressed {count}", 
                    command = counter,
                    activebackground = "yellow",
                    )


btn2 = tk.Button(win, text = "status", 
                command = disable_all,
                activebackground = "green")   

btn3 = tk.Button(win, text = "say_hello", 
                command = lambda:tk.Label(win, text = "Hello").pack(),
                activebackground = "green")                                  
b1.pack()
btn2.pack()
btn3.pack()
win.mainloop()