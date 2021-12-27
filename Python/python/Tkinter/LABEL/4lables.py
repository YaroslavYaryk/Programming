import tkinter as tk

win = tk.Tk()
win.title("My GUI")
win.geometry("+500+150")
win.resizable(False,False)
win.config(bg = "blue")

bottom_frame = tk.Frame(win)
top_frame = tk.Frame(win)
left_frame = tk.Frame(win)

bottom_frame.pack(padx = 5, pady = 5)
left_frame.pack(padx = 5,pady = 5)
top_frame.pack(padx = 5,pady = 5)

tk.Label(bottom_frame, text = "green", bg = "green", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(bottom_frame, text = "yellow", bg = "yellow", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(bottom_frame, text = "purple", bg = "purple", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(top_frame, text = "orange", bg = "blue", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(top_frame, text = "orange", bg = "white", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(top_frame, text = "orange", bg = "purple", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(left_frame, text = "orange", bg = "brown", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(left_frame, text = "orange", bg = "gray", width = 30, height = 10).pack(side = "left", padx = 5)
tk.Label(left_frame, text = "orange", bg = "pink", width = 30, height = 10).pack(side = "left", padx = 5)



win.mainloop()