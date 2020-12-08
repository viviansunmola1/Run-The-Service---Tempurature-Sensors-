import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# a = np.genfromtxt("sensors.csv", usecols=(2,3), skip_header=1, dtype=None, encoding=None)

df=pd.read_csv("sensors.csv")


# print(x,y)
plt.figure(figsize = (5,5)) # size of tab
plt.hist2d(x=df['x'],y = df['y'], bins = 50,)
plt.title('TEMPURATURE SERVICE - RTS')
plt.xlabel('X_POSITION')
plt.ylabel('Y_POSITION')
# cmap=plt.cm.get_cmap('RuBu',6)


plt.colorbar(label='Tempurature Values')
plt.show()