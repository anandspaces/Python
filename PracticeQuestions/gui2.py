#to use a tkinter entry in a program
from tkinter import *
tp = Tk()
la1 = Label(tp,text="user id")
la1.pack(side=LEFT)
en1 = Entry(tp,bd=6)
en1.pack(side=RIGHT)
tp.mainloop()