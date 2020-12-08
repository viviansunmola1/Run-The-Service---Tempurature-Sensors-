import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# a = np.genfromtxt("sensors.csv", usecols=(2,3), skip_header=1, dtype=None, encoding=None)

df=pd.read_csv("sensors.csv")


# print(x,y)

plt.figure(figsize = (5,5)) # size of histogram
plt.hist2d(x=df['x'],y = df['y'], bins = 50)


plt.colorbar()
plt.show()