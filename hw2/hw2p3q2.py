# -*- coding: utf-8 -*-
"""
Homework 2 Assignment III Part 2
Created on Thu Jan 30 15:05:45 2020

@author: Emily Springer
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.timeseries import LombScargle

A = 3
B = 100
L = 10
f = L / 2
t = np.arange(32768)
gaus = A * np.exp(-B * (t - f) ** 2)

y = []
with open('arecibo1.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = [float(s) for s in line.split()]
        y.append(values[0])


frequency, power = LombScargle(t, gaus).autopower(minimum_frequency=0, maximum_frequency=10)
frequency2, power2 = LombScargle(t, y).autopower(minimum_frequency=0, maximum_frequency=10)
plt.figure(1)
plt.ylabel('Lomb-Scargle Power')
plt.xlabel('frequency')
plt.title('Lomb-Scargle Gaussian')
plt.plot(frequency, power) 
plt.figure(2)
plt.plot(frequency2, power2)   
plt.ylabel('Lomb-Scargle Power')
plt.xlabel('frequency')
plt.title('Lomb-Scargle Data')

plt.show()
