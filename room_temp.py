import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


# read  sensor.csv file
plot_col= ["id", "x", "y"]
df=pd.read_csv("sensors.csv", usecols= plot_col, index_col= False)
#save x and y values of each sensor in coordinates ==
print(df)

#read csv file == yes
#save x and y values of each sensor in coordinates ==
# save temp of each sensor in tempurature value ==
# have color color values==
#have temp thresholds = blue, red , green ,amber ,yellow==
#if tempurature value is one of the threshold color==
    #heatmap plot sensor coord + threshold color. ==
 

