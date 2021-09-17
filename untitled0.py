# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:36:47 2021

@author: hp
"""

import matplotlib.pyplot as plt
import csv 

x=[]
y=[]

with open(r'C:\Users\hp\Desktop\plot.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter = ',')
      
    for row in plots:
        x.append(row[0])
        y.append((row[1]))

plt.plot(x, y, color = 'g', label = "Nft Sales")
plt.xlabel('Date')
plt.ylabel('Nft sold')
plt.title('chart')
plt.legend()
plt.show()
        
