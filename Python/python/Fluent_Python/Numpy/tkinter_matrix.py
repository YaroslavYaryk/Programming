import tkinter as tk
import numpy as np
from tkinter import messagebox

class Test:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title = "Test"
        self.root.geometry("500x500+150+150")
        self.root.config(bg = "pink")

    def run(self):
        self.get_entry()
        self.draw_label()
        self.press_button()
        self.root.mainloop()

    def draw_label(self):
        tk.Label(self.root, width = 2, text = "X1", bg = "pink").grid(row = 0, column = 1, padx = 5, pady = 10)
        tk.Label(self.root, width = 2, text = "X1", bg = "pink").grid(row = 1, column = 1, padx = 5, pady = 10)
        tk.Label(self.root, width = 2, text = "X1", bg = "pink").grid(row = 2, column = 1, padx = 5, pady = 10)
        tk.Label(self.root, width = 2, text = "X2", bg = "pink").grid(row = 0, column = 3, padx = 5, pady = 10)
        tk.Label(self.root, width = 2, text = "X2", bg = "pink").grid(row = 1, column = 3, padx = 5, pady = 10)
        tk.Label(self.root, width = 2, text = "X2", bg = "pink").grid(row = 2, column = 3, padx = 5, pady = 10)
        tk.Label(self.root, width = 5, text = "X3 = ", bg = "pink").grid(row = 0, column = 5, padx = 2, pady = 10)
        tk.Label(self.root, width = 5, text = "X3 = ", bg = "pink").grid(row = 1, column = 5, padx = 2, pady = 10)
        tk.Label(self.root, width = 5, text = "X3 = ", bg = "pink").grid(row = 2, column = 5, padx = 2, pady = 10)
  


    def get_entry(self):

        self.en1 = tk.Entry(self.root, width = 5);self.en1.grid(row = 0, column = 0, padx = 2, pady = 10)
        self.en2 = tk.Entry(self.root, width = 5);self.en2.grid(row = 1, column = 0, padx = 2, pady = 10)
        self.en3 = tk.Entry(self.root, width = 5);self.en3.grid(row = 2, column = 0, padx = 2, pady = 10)
        self.en4 = tk.Entry(self.root, width = 5);self.en4.grid(row = 0, column = 2, padx = 2, pady = 10)
        self.en5 = tk.Entry(self.root, width = 5);self.en5.grid(row = 1, column = 2, padx = 2, pady = 10)
        self.en6 = tk.Entry(self.root, width = 5);self.en6.grid(row = 2, column = 2, padx = 2, pady = 10)
        self.en7 = tk.Entry(self.root, width = 5);self.en7.grid(row = 0, column = 4, padx = 2, pady = 10)
        self.en8 = tk.Entry(self.root, width = 5);self.en8.grid(row = 1, column = 4, padx = 2, pady = 10)
        self.en9 = tk.Entry(self.root, width = 5);self.en9.grid(row = 2, column = 4, padx = 2, pady = 10)
        self.eny1 = tk.Entry(self.root, width = 5);self.eny1.grid(row = 0, column = 6, padx = 10, pady = 10)
        self.eny2 = tk.Entry(self.root, width = 5);self.eny2.grid(row = 1, column = 6, padx = 10, pady = 10)
        self.eny3 = tk.Entry(self.root, width = 5);self.eny3.grid(row = 2, column = 6, padx = 10, pady = 10)

            



    def main_operation(self):
        x_array = np.array([])
        y_array = np.array([])
        storage = [self.en1,  self.en4, self.en7, self.en2, self.en5,  self.en8, self.en3, self.en6, self.en9]
        for element in storage:
            x_array = np.append(x_array, int(element.get()))
        x_array.shape = 3,3 
        x_array = x_array.astype(np.int64)   
        storage = [self.eny1, self.eny2, self.eny3]    
        for  element in storage:
            y_array = np.append(y_array, int(element.get()))

        y_array = y_array.astype(np.int64)
        try:
            self.result_array = np.round(np.linalg.solve(x_array, y_array)).astype(np.int64)
        except np.linalg.LinAlgError:
            messagebox.showwarning("Warning", " Singular matrix")
        self.draw_result()


    def draw_result(self):
        tk.Label(self.root, width = 10, bg = "pink", font = ("Arial", 8, "bold") ,text =f"X1 = {self.result_array[0]}").grid(row = 6, column = 0)      
        tk.Label(self.root, width = 10, bg = "pink", font = ("Arial", 8, "bold") ,text =f"X2 = {self.result_array[1]}").grid(row = 7, column = 0)          
        tk.Label(self.root, width = 10, bg = "pink", font = ("Arial", 8, "bold") ,text =f"X3 = {self.result_array[2]}").grid(row = 8, column = 0)          



            



    def press_button(self):
        tk.Button(self.root, text = "Calculate", bg = "green", command = self.main_operation).grid(row = 5, column = 4, sticky ="nswe")


obj = Test()
obj.run()
