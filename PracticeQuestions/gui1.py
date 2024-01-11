#to work with button
import tkinter as tk
from tkinter import messagebox as bx
tp = tk.Tk()
def exbutton():
    bx.showinfo("hello world")
B = tk.Button(tp,text="press this button",command=exbutton)
B.pack()
tp.mainloop()
