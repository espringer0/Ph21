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

# creates a simulation of probability of getting each point
def getData(nPoints):
    angles = np.random.rand(nPoints) * np.pi #- np.pi/2
    B = 1.
    A = 1.
    return np.tan(angles) * B +A

def getPosterior(params, data):
    logB = 0
    if (params[1] > 0):
        logB = math.log(params[1])
    
    likelihood = np.ones(len(data)) * logB - np.ones(len(data)) * \
    math.log(math.pi) - np.log(params[1]**2 + (data - params[0]) ** 2)
    
    return np.sum(likelihood)

nPoints = 10000

data = []


n = 50
A = np.linspace(0, 5, nPoints)
B = np.linspace(0, 5, nPoints)

data = getData(n)
            
ndim = 2
nwalkers = 64 #number of chains 
chainLength = 10000
p0 = np.random.rand(nwalkers, ndim) * 5
sampler = emcee.EnsembleSampler(nwalkers, ndim, getPosterior, args = [data])
state = sampler.run_mcmc(p0, 100)
sampler.reset()

sampler.run_mcmc(state, chainLength)

samples = sampler.get_chain(flat=True)

maximumCoords = np.where(samples == np.amax(samples))
print(list(zip(maximumCoords[0], maximumCoords[1])))

print(len(samples))

fig = corner.corner(sampler.flatchain, labels=[r"$\alpha$", r"$\beta$"], bins=100)


    


