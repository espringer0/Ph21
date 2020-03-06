# -*- coding: utf-8 -*-
"""
Assignment 1 part 2
Created on Wed Mar  4 15:20:59 2020

@author: Emily Springer
"""

import numpy as np

def PCA(points):
    cov_mat = np.cov(points, rowvar=False)
    eigenvalues, eigenvectors = np.linalg.eig(cov_mat)
    order = np.argsort(-eigenvalues)
    eigenvalues = eigenvalues[order]
    eigenvectors = eigenvectors[:, order]
    return eigenvalues, eigenvectors 

def getData():
    x = np.random.rand()
    array = [x + getError(), 5 * x + 3 + getError()]
    return np.array(array)

def getError():
    sigma = 0.05
    mu = 0
    return np.random.normal(mu, sigma)
    
np.random.seed()
size = 10
points = np.ones((size, 2))
for i in range(size):
    points[i] = getData()
eigenvalue, eigenvectors = PCA(points)

print(eigenvalue)
print(eigenvectors) #principal components



