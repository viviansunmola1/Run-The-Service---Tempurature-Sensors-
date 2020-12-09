import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv("sensors.csv")

plt.figure(figsize = (5,5)) # size of tab
plt.hist2d(x=df['x'],y = df['y'], bins = 50,)
plt.get_cmap('RdBu')
plt.title('TEMPURATURE SERVICE - RTS')
plt.xlabel('X_POSITION')
plt.ylabel('Y_POSITION')
plt.colorbar(label='Tempurature Values')

blue_threshold = range (1,18)
green_threshold = range(19,26)
amber_threshold = range(27,30)
red_threshold = range(30, 100)
yellow = None


plt.show()

