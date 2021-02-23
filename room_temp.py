import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import*

tk = Tk()
tk.geometry('500x500')
tk.title('Tempsensors')

class ER_Options():
    def ER1():
        df = pd.read_csv('ER1.csv')
        pivot_table= df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        heatmap= sb.heatmap(pivot_table)
        title = "ER1 Server Room"
        plt.title(title,fontsize=10)
        plt.show()
        
    def ER2():
        df = pd.read_csv('ER2.csv')
        pivot_table= df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        heatmap= sb.heatmap(pivot_table)
        title = "ER2 Server Room"
        plt.title(title,fontsize=10)
        plt.show()
        
    def ER3():
        df = pd.read_csv('ER3.csv')
        pivot_table= df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        heatmap= sb.heatmap(pivot_table)
        title = "ER3 Server Room"
        plt.title(title,fontsize=10)
        plt.show()

def configButtons(): 
    btn=Button(tk, text="ER1", 
                command= ER_Options.ER1,
                height = 10, 
                width = 10)
    btn.pack()

    btn2= Button(tk,
                text="ER2",
                command = ER_Options.ER2,
                height = 10, 
                width = 10)
    btn2.pack()

    btn3= Button(tk, 
                text="ER3",
                command = ER_Options.ER3,
                height = 10, 
                width = 10)

    btn3.pack()

    btn.config(anchor=CENTER)

configButtons()
mainloop()











