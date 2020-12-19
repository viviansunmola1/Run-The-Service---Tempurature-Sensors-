import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

#read sensor.csv
df = pd.read_csv('sensors.csv')



#creating a pivot table 
pivot_table=df.pivot(index='y' ,columns= 'x', values = 'tempurature')

#colorbar ranges
crange= [0 18; 17 26; 27 30; 31 inf]
cmap = rand(size(crange,1),3)

#creating heatmap 
heatmap=sb.heatmap(pivot_table, annot=True)
title="RTS Tempurature Sensors ENTS Labs"
plt.title(title,fontsize=10)







plt.show()
# sb.heatmap(heatmap,annot=label, fmt="", cmap='RdY1Gn')




#read csv file == yes
#save x and y values of each sensor in coordinates ==
# save temp of each sensor in tempurature value ==
# have color color values==
#have temp thresholds = blue, red , green ,amber ,yellow==
#if tempurature value is one of the threshold color==
    #heatmap plot sensor coord + threshold color. ==
 

