import matplotlib.pyplot as plot
import numpy as num

def graph():
    x = num.array([10,20,30])
    y = num.array([200,250,500])
    plot.bar(x,y)
    plot.title("Anand")
    plot.show()

if __name__ == "__main__":
    graph()