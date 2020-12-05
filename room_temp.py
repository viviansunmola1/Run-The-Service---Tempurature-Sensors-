import csv 
import numpy as np
import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

# a = np.genfromtxt("sensors.csv", usecols=(2,3), skip_header=1, dtype=None, encoding=None)

df=pd.read_csv("sensors.csv")
coord=df[['x','y']]
print(coord)


