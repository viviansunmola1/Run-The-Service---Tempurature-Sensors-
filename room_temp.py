import csv 
import missingno as msno
import numpy as np
from numpy.lib.function_base import piecewise
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import tkinter as t
from tkinter import *

tk = Tk()
tk.geometry('500x500')
tk.title('ENTS Run The Service - Temperature Sensors')


newcolors = plt.get_cmap('viridis',36).colors

# newcolors[0: 18, :] = colors.to_rgba('blue')
# newcolors[18: 26, :] = colors.to_rgba('green')
# newcolors[27: 30] = colors.to_rgba('orange')
# newcolors[30:100, :] = colors.to_rgba('red')
# mycmap = colors.ListedColormap(newcolors)

newcolors[0] = colors.to_rgba('black')
newcolors[1:26] = colors.to_rgba('green')
newcolors[26:30 ] = colors.to_rgba('orange')
newcolors[30:] = colors.to_rgba('red')

mycmap = colors.ListedColormap(newcolors)


class ER_Options():
    def ER1():
        df = pd.read_csv('ER1.csv')
        pivot_table= df.pivot(index='Position_y',
                            columns= 'Position_x', 
                            values = 'Temperature')

       
        pivot_table = pivot_table.replace(r'^\s*$', np.nan, regex=True)
        pivot_table = pivot_table.astype(float)
        pivot_table.fillna(0, inplace=True)
        
    

        heatmap= sb.heatmap(pivot_table,
                            annot=True,
                            cmap=mycmap,
                            fmt = ".1f",
                            cbar_kws= {'pad': .01, 'ticks': [0,1, 26, 30], })

        for Tempurature in pivot_table.to_records():
            print(Tempurature)
            try:
                if 28 in pivot_table:
                    print("NaN value found")
                else:
                    print("NaN values is not in this field")
            except Exception as e:
                newcolors[2] = colors.to_rgba('purple')



        heatmap.collections[0].colorbar.set_label("Temperature Thresholds")
        plt.gca().invert_yaxis()

        title = "ER1 Server Room"
        plt.title(title,fontsize=10)

        
        plt.show()



    def ER2():
        df = pd.read_csv('ER2.csv')
        pivot_table= df.pivot(index='Position_y',
                            columns= 'Position_x', 
                            values = 'Temperature')

        pivot_table = pivot_table.replace(r'^\s*$', np.nan, regex=True)
        pivot_table = pivot_table.astype(float)
        pivot_table.fillna(0, inplace=True)

        heatmap= sb.heatmap(pivot_table,
                            annot=True,
                            cmap='rainbow',
                            fmt = ".1f",
                            cbar_kws= {'pad': .03, 'ticks': [0,18, 26, 27, 30, 100], })


        heatmap.collections[0].colorbar.set_label("Temperature Thresholds")
        plt.gca().invert_yaxis()

        title = "ER2 Server Room"
        plt.title(title,fontsize=10)
        plt.show()
        
    def ER3():
        df = pd.read_csv('ER3.csv')
        pivot_table= df.pivot(index='Position_y',
                            columns= 'Position_x', 
                            values = 'Temperature')

        heatmap= sb.heatmap(pivot_table,
                            annot=True,
                            cmap='rainbow',
                            fmt = ".1f",
                            cbar_kws= {'pad': .01, 'ticks': [0,18, 26, 27, 30, 100], })


        heatmap.collections[0].colorbar.set_label("Temperature Thresholds")
        plt.gca().invert_yaxis()
    

        title = "ER3 Server Room"
        plt.title(title,fontsize=10)
        plt.show()

def configButtons(): 
    btn=Button(tk, 
                text="ER1", 
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











