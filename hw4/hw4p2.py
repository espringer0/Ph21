# -*- coding: utf-8 -*-
"""
Homework 4 Part 2
Created on Thu Feb 20 15:28:49 2020

@author: Emily Springer
"""

import random
import matplotlib.pyplot as plt
import math
import numpy as np

# creates a simulation of probability of getting each point
def getData(nPoints):
    allPoints = []
    angles = np.linspace(0, math.pi, 10000)
    B = 1
    A = 1
    for i in range(nPoints):
        randIdx = random.randint(0, nPoints - 1)
        x = math.tan(angles[randIdx]) * B + A
        allPoints.append(x)
    return allPoints
      
nPoints = 10000
allPoints = getData(nPoints)

data = []

n = 32
A = np.linspace(0, 5, nPoints)

for i in range(n):
    randIdx = random.randint(0, len(allPoints) - 1)
    data.append(allPoints[randIdx])
    
sumPart = 0
averageX = 0
for pt in data:
    sumPart += 1 + ((pt) - A) ** 2
    averageX += pt
averageX /= len(data)
        
likelihood = math.log(1) - math.log(math.pi) - sumPart

# pre-normalize
maximum = -100000
for j in range (n):
    if (likelihood[j] > maximum):
        maximum = likelihood[j]

posterior = likelihood - maximum
for i in range(len(posterior)):
    posterior[i] = math.exp(posterior[i])

# post-normalize
normalization = 0
for i in range(len(posterior)):
    normalization += posterior[i]
normalization /= nPoints
# average value
print(averageX)

plt.plot(A, posterior / normalization)
plt.xlabel("alpha value")
plt.ylabel("likelihood")
plt.show()

