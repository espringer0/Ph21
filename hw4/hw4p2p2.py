# -*- coding: utf-8 -*-
"""
Homework 4 Part 2 of Part 2
Created on Fri Feb 21 15:58:45 2020

@author: Emily Springer
"""

import random
import matplotlib.pyplot as plt
import math
import numpy as np

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

def getLikelihood(a, b, data):
    logB = 0
    if (b > 0):
        logB = math.log(b)
    likelihood = logB - math.log(math.pi) - sum(b**2 + (data - a) ** 2)
    return likelihood

nPoints = 1000
allPoints = getData(nPoints)

data = []

n = 32
A = np.linspace(0, 5, nPoints)
B = np.linspace(0, 5, nPoints)

for i in range(n):
    randIdx = random.randint(0, len(allPoints) - 1)
    data.append(allPoints[randIdx])

averageX = 0
for pt in data:
    averageX += pt    
likelihood = np.array([[getLikelihood(a, b, data)for a in A ]for b in B])

# pre-normalize
maximum = -100000
for j in range (n):
    for i in range (n):
        if (likelihood[j][i] > maximum):
            maximum = likelihood[j][i]
posterior = likelihood + maximum
for i in range(len(posterior)):
    posterior[i][0] = math.exp(posterior[i][0])

#post-normalize
normalization = 0
for i in range(len(posterior)):
    for j in range(len(posterior)):
        normalization += posterior[i][j]
normalization /= nPoints ** 2
averageX /= n
print(averageX)
posterior /= normalization

# contour plot
fig = plt.figure(figsize=(8,8))
ax = fig.gca()
xmin, ymin = 0, 0
xmax, ymax = 5, 5
ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)
cfset = ax.contourf(A, B, posterior, cmap='coolwarm')
ax.imshow(np.rot90(posterior), cmap='coolwarm', extent=[xmin, xmax, ymin, ymax])
cset = ax.contour(A, B, posterior, colors='k')
ax.clabel(cset, inline=1, fontsize=10)
ax.set_xlabel('A')
ax.set_ylabel('B')
plt.title('2D Posterior Distribution')

