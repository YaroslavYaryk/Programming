import tkinter as tk
import  numpy as np
from time import sleep

arr_x = np.zeros((3,3), dtype=np.int8)
arr_zero = np.zeros((3,3), dtype=np.int8)


counter = 0

class Window(object):
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.root.geometry("355x300+550+250")
        self.root.configure(bg = "pink")
        self.run()
    
    def run(self):
        self.draw_buttons()
        self.root.mainloop()

    def draw_winner(self,value):
        win = tk.Toplevel(self.root)
        win.title("Winner")
        win.geometry("355x300+550+250")
        win.configure(bg = "green")
        win.protocol("WM_DELETE_WINDOW", self.close_window)

        if value == "win":
            if self.check_win(arr_x):
                tk.Label(win, text = "X", bg = "green", font = ("Arial", 40, "bold"),fg = "red", anchor = "center").place(relx = 0.45, rely = 0.4 )
            else:
                tk.Label(win, text = "O", bg = "green",font = ("Arial", 40, "bold"), fg = "red" ,anchor = "center").place(relx = 0.43, rely = 0.37 )
                
        elif value == "dead heat":
            tk.Label(win, text = "dead heat", bg = "green", font = ("Arial", 30, "bold"),fg = "red" ,anchor = "center").place(relx = 0.27, rely = 0.4 )




    def draw_figure(self, varible, coord1, coord2):
        global counter
        global arr_x
        global arr_zero
        if counter %2 == 0:
            varible.configure(text = "X",disabledforeground = "red", state = tk.DISABLED)
            arr_x[coord1][coord2] = 1
            counter +=1
        else:
            varible.configure(text = "O",disabledforeground = "red", state = tk.DISABLED)
            counter +=1
            arr_zero[coord1][coord2] = 1

        if self.check_win(arr_x) or self.check_win(arr_zero):
            self.draw_winner("win")
        elif (sum(sum(arr_x)) == 5 and sum(sum(arr_zero)) ==4
        or sum(sum(arr_x)) == 4 and sum(sum(arr_zero)) == 5 ):
            self.draw_winner("dead heat")



    def check_win(self, variable):
        global arr_x
        if (sum(variable[:3,:1]) == 3 or sum(variable[0]) == 3  or sum(variable[0:,1]) == 3
            or sum(variable[0:,2]) == 3 or sum(variable[1]) == 3 or sum(variable[2]) == 3
            or (variable[0,0] +  variable[1,1] +  variable[2,2] == 3) or (variable[0,2] +  variable[1,1] +  variable[2,0] == 3) ):

            return True
        return False
            

    def close_window(self):
        self.root.destroy()    

    def draw_temple_button(self):
        return  tk.Button(self.root, activebackground = "white", activeforeground = "white", text = "O" ,
        bg = "white", font = "100",fg = "white",padx = 44, pady = 31)   


    def draw_buttons(self):
        self.a11 = self.draw_temple_button();self.a11.grid(sticky = "nswe", row = 0, column = 0);self.a11.configure( command = lambda: self.draw_figure(self.a11, 0,0))
        self.a12 = self.draw_temple_button();self.a12.grid(sticky = "nswe", row = 0, column = 1);self.a12.configure( command = lambda: self.draw_figure(self.a12, 0,1))
        self.a13 = self.draw_temple_button();self.a13.grid(sticky = "nswe", row = 0, column = 2);self.a13.configure( command = lambda: self.draw_figure(self.a13, 0,2))
        self.a21 = self.draw_temple_button();self.a21.grid(sticky = "nswe", row = 1, column = 0);self.a21.configure( command = lambda: self.draw_figure(self.a21, 1,0))
        self.a22 = self.draw_temple_button();self.a22.grid(sticky = "nswe", row = 1, column = 1);self.a22.configure( command = lambda: self.draw_figure(self.a22, 1,1))
        self.a23 = self.draw_temple_button();self.a23.grid(sticky = "nswe", row = 1, column = 2);self.a23.configure( command = lambda: self.draw_figure(self.a23, 1,2))
        self.a31 = self.draw_temple_button();self.a31.grid(sticky = "nswe", row = 2, column = 0);self.a31.configure( command = lambda: self.draw_figure(self.a31, 2,0))
        self.a32 = self.draw_temple_button();self.a32.grid(sticky = "nswe", row = 2, column = 1);self.a32.configure( command = lambda: self.draw_figure(self.a32, 2,1))
        self.a33 = self.draw_temple_button();self.a33.grid(sticky = "nswe", row = 2, column = 2);self.a33.configure( command = lambda: self.draw_figure(self.a33, 2,2))
activeforeground = "white",


Window()
