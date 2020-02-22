# -*- coding: utf-8 -*-
"""
Homework 4 Part 1
Created on Wed Feb 19 15:18:20 2020


@author: Emily Springer
"""

import random
import matplotlib.pyplot as plt
import math
import numpy as np

n = 32
nHeads = 0;
for i in range(n):
    rand = random.randint(0, 1)
    if (rand == 1):
        nHeads += 1
        
probHeads = nHeads / n;
nPoints = 1000
H = np.linspace(0, 1, nPoints)
#prior = 0.5
sigma = 0.1
mu = 0.5 # change mean for how many sigma away from "true" H value it is
norm = 0
#prior = np.asarray([0.5] * nPoints)
prior = 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (H - mu)**2 / (2 * sigma**2) )
for j in range (nPoints):
        norm += prior[j] * 0.001
prior /= norm

# change with time
for i in range(5):
    normalization = 0
    likelihood = math.factorial(n) / (math.factorial(nHeads) * \
                           math.factorial(n - nHeads)) * H ** nHeads * \
                           (1 - H) ** (n - nHeads)
        
    plt.plot(H, prior, 'r')
    
    for j in range (nPoints):
        normalization += likelihood[j] * prior[j] * 0.001
        
    prob = likelihood * prior / normalization
    plt.plot(H, prob, 'g')
    plt.show()
    prior = prob # take this out for one time distribution
    
    