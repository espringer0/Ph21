# -*- coding: utf-8 -*-
"""
Homework 5 Part 1
Created on Thu Feb 27 15:35:14 2020

@author: Emily Springer
"""

import random
import matplotlib.pyplot as plt
import numpy as np
import emcee
import math


def getPosterior(a, nHeads):
    sigma = 0.3
    mu = 0.5
    prior = -(np.log(sigma) + np.log(np.sqrt(2 * np.pi)))\
    - (a - mu)**2 / (2 * sigma**2)
    if a <= 0 or a >=1:
        return -np.inf

    likelihood = np.log(math.factorial(n)) -(np.log((math.factorial(nHeads)) + \
                           np.log (math.factorial(n - nHeads)))) + \
                           nHeads * np.log(a)  + (n - nHeads) * np.log(1 - a)
    return prior + likelihood

n = 10
nHeads = 0
for i in range(n):
    rand = random.randint(0, 1)
    if (rand == 1):
        nHeads += 1
            
ndim = 1
nwalkers = 64 #number of chains 
chainLength = 10000
p0 = np.random.rand(nwalkers, ndim)
sampler = emcee.EnsembleSampler(nwalkers, ndim, getPosterior, args = [nHeads])
state = sampler.run_mcmc(p0, 100)
sampler.reset()

sampler.run_mcmc(state, chainLength);

samples = sampler.get_chain(flat=True)
plt.hist(samples[:, 0], 100, color="k", histtype="step")
plt.gca().set_yticks([]);
plt.xlabel(r"Percentage of Heads")
plt.ylabel(r"Probability")
plt.title('Coin Toss Problem with MCMC')

print("Mean acceptance fraction: {0:.3f}"
                .format(np.mean(sampler.acceptance_fraction)))
    