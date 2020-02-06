# -*- coding: utf-8 -*-
"""
Homework 2 Assignment II Part 2
Created on Wed Jan 29 16:45:29 2020

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

plt.plot(abs(spectrum))
plt.ylabel('magnitude')
plt.xlabel('frequency (Hz)')
plt.title('Fourier Transformed Data')

dt = 0.16
L = 1.
f = L / 2
frequency = 3964.5
t = np.linspace(0,L,10000)

# A * exp[−B(t − L/2)^2]
sp = np.fft.fft(1.3*(np.sin(frequency * 2 * np.pi * t)) * \
                np.exp(-1 * (t - f) ** 2 / dt ** 2))

freq = np.fft.fftfreq(t.shape[-1], L/30000.)
plt.plot(freq + 16384, abs(sp))
#plt.xlim([28270,28290])
#plt.xlim([4480,4500])
plt.show()