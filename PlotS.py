# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 16:50:20 2021

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
import csv 

x=[]
y=[]
z=[]

with open(r'C:\Users\hp\Desktop\plot.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append((row[1]))
        z.append((row[2]))
    
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(x, y, 'g-')
ax2.plot(x, z, 'b-')

ax1.set_xlabel('Date')
ax1.set_ylabel('Sales', color='g')
ax2.set_ylabel('Sentiment', color='b')

plt.show()