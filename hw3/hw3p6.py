# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:17:39 2020


@author: Emily Springer
"""

import PIL
from PIL import ImageFilter
import numpy as np
from scipy import ndimage

def sobel_filters(img):
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)
    
    
    pix = np.array(img)
    pix2 = [[0 for x in range(len(pix[0]))] for y in range(len(pix))]
    for i in range(len(pix)):
        for j in range(len(pix[i])):
            pix2[i][j] = (int)(pix[i][j][0])
    
    Ix = ndimage.filters.convolve(pix2, Kx)
    Iy = ndimage.filters.convolve(pix2, Ky)
    
    G = np.hypot(Ix, Iy)
    G = G / G.max() * 255
    
    for i in range(len(G)):
        for j in range(len(G[i])):
            if (G[i][j] < 15):
                G[i][j] = 0
    
    image = PIL.Image.fromarray(G)
    
    return (image)

im = PIL.Image.open(r"C:\Caltech\Ph21\hw3\image.jpg")

blurred = im.filter(ImageFilter.GaussianBlur(1.5))

image = sobel_filters(blurred)
image.show()