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

blue_threshold = all(df['x'] <= 18)
green_threshold = all(df['x']== range(19,26))
amber_threshold = all(df['x'] == range(27,30))
red_threshold = all(df['x'] > 30)
print(blue_threshold)





# cmap = matplotlib.colors.ListedColormap(['Blue', 'Green', 'Amber', 'Red', 'Yellow', 'Black'])


# plt.show()

