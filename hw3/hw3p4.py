# -*- coding: utf-8 -*-
"""
Homework 3 Part 4
Created on Wed Feb 12 14:32:43 2020


@author: Emily Springer
"""

import PIL
from PIL import ImageFilter

im = PIL.Image.open(r"C:\Caltech\Ph21\hw3\image.jpg")

blurred = im.filter(ImageFilter.GaussianBlur)

blurred.show()