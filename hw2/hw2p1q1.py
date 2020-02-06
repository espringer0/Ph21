# -*- coding: utf-8 -*-
"""
Homework 2 Assignment I Part 1
Created on Wed Jan 22 21:20:56 2020

@author: Emily Springer
"""
import numpy as np
import matplotlib.pyplot as plt


C = 5
A = 1
B = 1
L = 10.
f = L / 2
phi = 0
t = np.arange(256)

# C + Acos(ft + phi))
sp = np.fft.fft(C + A * np.cos(f * t + phi))
freq = np.fft.fftfreq(t.shape[-1])
plt.plot(freq, sp.real, freq, sp.imag)
plt.ylabel('magnitude')
plt.xlabel('frequency (Hz)')
plt.title('Fourier Transformed Cosine')
plt.show()

# A * exp[−B(t − L/2)^2]
y = A * np.exp(-B * (t - f) ** 2)
y_fft = (np.abs(np.fft.fft(y))) / np.sqrt(len(y))
plt.plot(freq,y_fft)
plt.title('Fourier Transformed Gaussian')
plt.show()

