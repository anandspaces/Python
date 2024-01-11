#to program using label and grid
import tkinter as tk
m = tk.Tk()
tk.Label(m,text = "first",bg = "red").grid(row = 0,column = 0)
tk.Label(m,text = "second",bg = "blue").grid(row = 0,column = 1)
tk.Label(m,text = "third",bg = "green").grid(row = 1,column = 0)
m.mainloop()