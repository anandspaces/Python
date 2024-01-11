#to program using checkbutton with grid sticky option
from tkinter import *
m = Tk()
var1 = IntVar()
var2 = IntVar()
Label(m,text = "your sex: ").grid(row = 0,sticky = W)
Checkbutton(m,text = "male",variable = var1).grid(row = 1,sticky = W)
Checkbutton(m,text = "female",variable = var2).grid(row = 2,sticky = W)
mainloop()