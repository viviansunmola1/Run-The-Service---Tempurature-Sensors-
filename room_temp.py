import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


# read file
df=pd.read_csv("sensors.csv")

# get x and y colomns for each sensor 
# get temp reading for each sensor 


plt.figure(figsize = (5,5)) # size of tab

plt.hist2d(x=df['x'],y = df['y'], bins = 50,)
plt.get_cmap('RdBu')
plt.title('TEMPURATURE SERVICE - RTS')
plt.xlabel('X_POSITION')
plt.ylabel('Y_POSITION')

plt.colorbar()
plt.show()
