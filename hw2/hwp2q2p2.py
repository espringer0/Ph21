# -*- coding: utf-8 -*-
"""
Homework 2 Assignment II Part 1
Created on Wed Jan 29 15:52:42 2020

@author: Emily Springer
"""

import numpy as np
import matplotlib.pyplot as plt

y = []
with open('arecibo1.txt') as f:
    lines = f.readlines()
    for line in lines:
        values = [float(s) for s in line.split()]
        y.append(values[0])

spectrum =np.fft.fft(y)

ff_ii = np.where(np.abs(spectrum) > 1000.0)[0][0] # Just get one frequency, the other one is just mirrored freq at negative value
print('frequency of:', ff_ii)

plt.plot(spectrum)
plt.ylabel('magnitude')
plt.xlabel('frequency (Hz)')
plt.title('Fourier Transformed Data')
plt.show()