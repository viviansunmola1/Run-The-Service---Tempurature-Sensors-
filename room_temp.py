import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sensors.csv')
sensor = ((np.asarray(df['sensor_id'])).reshape(3,3))
tempurature = ((np.asarray(df['tempurature'])).reshape(3,3))

#temp thresholds
blue = range(0, 10)
red = range(11,20)

#creating a pivot table 
heatmap = df.pivot(index='y' ,columns= 'x', values = 'tempurature')
# temp = heatmap.values
label = (np.asarray(["{0} \n{1:2.f}".format(sens,temp)
                    for sens,temp in zip(sensor.flatten(), 
                                            tempurature.flatten())]
        ).reshape(3,3)



#creating heatmap 
fig,ax = plt.subplots(figsize=(3,3))

title = "RTS Tempurature Sensors ENTS Labs"
plt.title(title,fontsize=10)
sb.heatmap(heatmap,annot=True, fmt="", cmap='RdY1Gn')


plt.show()

#read csv file == yes
#save x and y values of each sensor in coordinates ==
# save temp of each sensor in tempurature value ==
# have color color values==
#have temp thresholds = blue, red , green ,amber ,yellow==
#if tempurature value is one of the threshold color==
    #heatmap plot sensor coord + threshold color. ==
 

