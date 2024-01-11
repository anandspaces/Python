#assigning checkbutton selection to variable
from tkinter import *
m = Tk()
def var_states():
    print(var1.get())
    print(var2.get())
Label(m,text = "your sex: ").grid(row = 0,sticky = W)
var1 = IntVar()
Checkbutton(m,text = "male",variable = var1).grid(row = 1,sticky = W)
var2 = IntVar()
Checkbutton(m,text = "female",variable = var2).grid(row = 2,sticky = W)
Button(m,text = "show",command = var_states).grid(row = 4,sticky = W,pady = 4)
mainloop()