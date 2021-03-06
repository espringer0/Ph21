# -*- coding: utf-8 -*-
"""
Homework 5 Part 2
Created on Fri Feb 28 20:03:33 2020

@author: Emily Springer
"""

import matplotlib.pyplot as plt
import numpy as np
import emcee
import math
import corner
from scipy.optimize import minimize

# creates a simulation of probability of getting each point
def getData(nPoints):
    angles = np.random.rand(nPoints) * np.pi #- np.pi/2
    B = 1.
    A = 1.
    return np.tan(angles) * B + A

def getPosterior(params, data):
    logB = 0
    if (params[1] > 0):
        logB = math.log(params[1])
    else:
        return -np.inf
    likelihood = np.ones(len(data)) * logB - np.ones(len(data)) * \
    math.log(math.pi) - np.log(params[1]**2 + (data - params[0]) ** 2)
    
    return np.sum(likelihood)

nPoints = 1000

data = []


n = 1000
A = np.linspace(0, 5, nPoints)
B = np.linspace(0, 5, nPoints)

data = getData(n)


x_true = 1
y_true = 1
f_true = 0.5
x = np.sort(10 * np.random.rand(n))
yerr = 0.1 + 0.5 * np.random.rand(n)
y = x_true * x + y_true

           
ndim = 2
nwalkers = 32 #number of chains 
chainLength = 1000
p0 = np.random.rand(nwalkers, ndim) * 5
sampler = emcee.EnsembleSampler(nwalkers, ndim, getPosterior, args = [data])
state = sampler.run_mcmc(p0, 100)
sampler.reset()

sampler.run_mcmc(state, chainLength)

samples = sampler.get_chain(flat=True)

alpha = np.ones(len(samples))
beta = np.ones(len(samples))

for i in range(len(samples)):
    string = np.array2string(samples[i])
    split = string[1:-1].split()
    alpha[i] = float(split[0])
    beta[i] = float(split[1])
    
print("MEDIANS")
print(np.median(alpha))
print(np.median(beta))

maximumCoords = np.where(samples == np.amax(samples))

fig = corner.corner(sampler.flatchain, labels=[r"$\alpha$", r"$\beta$"], bins=100)


    


