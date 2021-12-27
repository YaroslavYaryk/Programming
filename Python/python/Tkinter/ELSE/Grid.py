import tkinter as tk

win = tk.Tk()
win.title("My GUI")
win.geometry("500x500+500+150")
win.resizable(False,False)
win.config(bg = "purple")
win.resizable(True, True)


l1 = tk.Entry(win, text = "green", bg = "green").grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = "WENS")

l1 = tk.Button(win, text = "green", bg = "green", width = 20, height = 5).grid(row = 3, column = 1, padx = 5, pady = 5)
l2 = tk.Button(win, text = "yellow", bg = "yellow", width = 20, height = 5).grid(row = 3, column = 2, padx = 5, pady = 5)
l3 = tk.Button(win, text = "blue", bg = "blue", width = 20, height = 5).grid(row = 3, column = 3, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "black", width = 20, height = 5).grid(row = 4, column = 1, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "white", width = 20, height = 5).grid(row = 4, column = 2, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "orange", width = 20, height = 5).grid(row = 4, column = 3, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "gray", width = 20, height = 5).grid(row = 5, column = 1, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "red", width = 20, height = 5).grid(row = 5, column = 2, padx = 5, pady = 5)
l4 = tk.Button(win, text = "pink", bg = "pink", width =  20, height = 5).grid(row = 5, column = 3, padx = 5, pady = 5)



win.mainloop()