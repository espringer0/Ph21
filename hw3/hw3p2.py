# -*- coding: utf-8 -*-
"""
Homework 3 Parts 2 & 3
Created on Wed Feb 12 14:21:04 2020

@author: Emily Springer
"""

import PIL
from PIL import ImageFilter

im = PIL.Image.open(r"C:\Caltech\Ph21\hw3\image.jpg")

print(im.format, im.size, im.mode)

imageWithEdges = im.filter(ImageFilter.FIND_EDGES)
im.show()
imageWithEdges.show()

