#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:03:19 2020

@author: augustinjose
"""


from Resize.bilinear import Bilinear
from Transform.grayscale import Grayscale
from Transform.gaussian import GaussianBlurImage
from Difference.FilterDiff import filterDiff

import cv2

img = cv2.imread("Input/test.jpg")
s =1.3
sigma = 1.6
k = 2**(1/s)
val = k * sigma
octave = 4
Pyramid = []

img = Grayscale(img)
layer = img
for i in range(octave):
    layer = GaussianBlurImage(layer, val)
    Pyramid.append(layer)
Diff = []
for j in range(len(Pyramid)-1):
    diff = filterDiff(Pyramid[j+1], Pyramid[j])
    Diff.append(diff)


    
    