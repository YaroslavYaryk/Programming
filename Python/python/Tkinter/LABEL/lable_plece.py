import tkinter as tk

win = tk.Tk()
win.title("My GUI")
win.geometry("500x500+500+150")
win.resizable(False,False)
win.config(bg = "blue")
win.resizable(True, True)



l1 = tk.Label(win, text = "green", bg = "green", width = 50, height = 20).place(relx = 0.1, rely = 0.2)
l2 = tk.Label(win, text = "yellow", bg = "yellow", width = 30, height = 10).place(in_ = l1,relx = 0.25, rely = 0.35)


win.mainloop()