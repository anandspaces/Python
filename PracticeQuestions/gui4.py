#to describe how to program using label and checkbutton in tkinter gui
from tkinter import *
m = Tk()
Label(m,text = "your sex: ").grid(row = 0)
Checkbutton(m,text = "male").grid(row = 1)
Checkbutton(m,text = "female").grid(row = 2)
mainloop()