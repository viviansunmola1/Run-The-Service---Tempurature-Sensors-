import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import*

#read from sensors file 
er1 = pd.read_csv('ER1.csv')
er2 = pd.read_csv('ER2.csv')
er3 = pd.read_csv('ER3.csv')

tk = Tk()
tk.title('Tempsensors')
def ER_Options():
    exit()

btn=Button(tk, text="ER1", 
            command= ER_Options)
btn.pack()

btn2= Button(tk, text="ER2",
            command = ER_Options)
btn2.pack()

btn3= Button(tk, text="ER3",
            command = ER_Options)
btn3.pack()

mainloop()











