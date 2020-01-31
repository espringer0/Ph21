# -*- coding: utf-8 -*-
"""
Homework 2 Assignment II Part 1
Created on Wed Jan 29 15:48:49 2020

@author: Emily Springer
"""

import matplotlib.pyplot as plt

x = []
y = []
i = 0;
with open('arecibo1.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = [float(s) for s in line.split()]
        x.append(i)
        y.append(values[0])
        i += 1;
        
    
#print(y)
plt.plot(x ,y)
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time')
plt.title('Data vs Time')
plt.show()