import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import*

# #read from sensors file 
# er1 = pd.read_csv('ER1.csv')
# er2 = pd.read_csv('ER2.csv')
# er3 = pd.read_csv('ER3.csv')

tk = Tk()
tk.title('Tempsensors')

class ER_Options():
    def ER1():
        plt.plot([1,2,3,4])
        plt.ylabel('some numbers')
        plt.show()

        # df = pd.read_csv('ER1.csv')
        # pivot_table = df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        # heatmap= sb.heatmap(pivot_table)
        # title = "RTS Tempurature Sensors ENTS Labs"
        # plt.title(title,fontsize=10)
        # plt.show()
        
    def ER2():
        df = pd.read_csv('ER2.csv')
        pivot_table = df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        heatmap= sb.heatmap(pivot_table)
        title = "RTS Tempurature Sensors ENTS Labs"
        plt.title(title,fontsize=10)
        plt.show()
        
    def ER3():
        df = pd.read_csv('ER3.csv')
        pivot_table = df.pivot(index='Position_y' ,columns= 'Position_x', values = 'Tempurature')
        heatmap= sb.heatmap(pivot_table)
        title = "RTS Tempurature Sensors ENTS Labs"
        plt.title(title,fontsize=10)
        plt.show()
        
        
btn=Button(tk, text="ER1", 
            command= ER_Options.ER1)
btn.pack()

btn2= Button(tk, text="ER2",
            command = ER_Options.ER2)
btn2.pack()

btn3= Button(tk, text="ER3",
            command = ER_Options.ER3)
btn3.pack()

mainloop()











