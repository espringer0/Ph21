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

dt = 0.213
L = 1.
f = L / 2
frequency = 3970.
t = np.linspace(0,L,10000)

# A * exp[−B(t − L/2)^2]
sp = np.fft.fft((np.sin(frequency * 2 * np.pi * t)) * \
                np.exp(-1 * (t - f) ** 2 / dt ** 2))

freq = np.fft.fftfreq(t.shape[-1], L/30000.)
#freq = np.fft.ifftshift(freq)
plt.plot(freq + 16380, abs(sp))
plt.show()