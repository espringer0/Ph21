# -*- coding: utf-8 -*-
"""
Assignment 1 part 4
Created on Thu Mar  5 14:34:48 2020

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

def getData(slope, yIntercept):
    x = np.random.rand()
    array = [x + getError(), slope * x + yIntercept + getError()]
    return np.array(array)

def get3DimsData():
    return np.concatenate((getData(3, 5), getData(-4, 10), getData(5, -2)))

def getError():
    sigma = 0.05
    mu = 0
    return np.random.normal(mu, sigma)
    
np.random.seed()
size = 10
points = np.ones((size, 6))
for i in range(size):
    points[i] = get3DimsData()
    
eigenvalue, eigenvectors = PCA(points)

print(eigenvalue)
print(eigenvectors)



