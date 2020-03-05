# -*- coding: utf-8 -*-
"""
Homework 5 Part 2
Created on Tue Mar  3 15:39:56 2020
@author: Emily Springer
"""

import matplotlib.pyplot as plt
import numpy as np
import emcee
import math
import corner

# creates a simulation of probability of getting each point
def getData(n):
    angles = np.random.rand(n) * np.pi #- np.pi/2
    B = 1.
    A = 3.
    return np.tan(angles) * B +A

def getDataInterloper(n):
    angles = np.random.rand(n) * np.pi #- np.pi/2
    B = 10.
    A = 15.
    return np.tan(angles) * B +A

def getPosterior(params, data):
    logB = 0
    if (params[1] > 0):
        logB = math.log(params[1])
    else:
        return -np.inf
    
    likelihood = np.ones(len(data)) * logB - np.ones(len(data)) * \
    math.log(math.pi) - np.log(params[1]**2 + (data - params[0]) ** 2)
    
    return np.sum(likelihood)

nPoints = 10000

data = []


n = 1000
A = np.linspace(0, 5, nPoints)
B = np.linspace(0, 5, nPoints)

data = np.append(getData(n), getDataInterloper(n))
            
ndim = 2
nwalkers = 200 #number of chains 
chainLength = 1000
p0 = np.random.rand(nwalkers, ndim) * 20
sampler = emcee.EnsembleSampler(nwalkers, ndim, getPosterior, args = [data])
state = sampler.run_mcmc(p0, 100)
sampler.reset()

sampler.run_mcmc(state, chainLength)

samples = sampler.get_chain(flat=True)

maximumCoords = np.where(samples == np.amax(samples))
print(list(zip(maximumCoords[0], maximumCoords[1])))

print(len(samples))

fig = corner.corner(sampler.flatchain, labels=[r"$\alpha$",  r"$\beta$"], bins=100)


    