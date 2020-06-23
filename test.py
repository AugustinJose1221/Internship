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
imgcopy = cv2.imread("Input/test.jpg")
s =1.3
sigma = 1.6
k = 2**(1/s)
val = k * sigma
octave = 4
Pyramid = []

img = Grayscale(img)
height = img.shape[0]
width = img.shape[1]
layer = img
for i in range(octave):
    layer = GaussianBlurImage(layer, val)
    #name = "Test/img/layer"+str(i)+".jpg"
    #cv2.imwrite(name, layer)
    Pyramid.append(layer)
Diff = []
for j in range(len(Pyramid)-1):
    diff = filterDiff(Pyramid[j+1], Pyramid[j])
    #Name = "Test/img/Interdiff"+str(j)+".jpg"
    #cv2.imwrite(Name, diff)
    Diff.append(diff)

keypoints =[]
L0 = Diff[0]
L1 = Diff[1]
L2 = Diff[2]
x = 0
y = 0
for i in range(1, height-1):
    
    if x%3!=0:
        x=x+1
        continue
    x=x+1
    
    for j in range(1, width-1):
        
        if y%3!=0:
            y=y+1
            continue
        y=y+1
        
        Pixel0 = max(L0[i-1][j-1], L0[i-1][j], L0[i-1][j+1],
                     L0[i][j-1], L0[i][j], L0[i][j+1],
                     L0[i+1][j-1], L0[i+1][j], L0[i+1][j+1])
        Pixel1 = max(L1[i-1][j-1], L1[i-1][j], L1[i-1][j+1],
                     L1[i][j-1], L1[i][j+1],
                     L1[i+1][j-1], L1[i+1][j], L1[i+1][j+1])
        Pixel2 = max(L2[i-1][j-1], L2[i-1][j], L2[i-1][j+1],
                     L2[i][j-1], L2[i][j], L2[i][j+1],
                     L2[i+1][j-1], L2[i+1][j], L2[i+1][j+1])
        Pixelval = max(Pixel0, Pixel1, Pixel2)
        
        pixel0 = min(L0[i-1][j-1], L0[i-1][j], L0[i-1][j+1],
                     L0[i][j-1], L0[i][j], L0[i][j+1],
                     L0[i+1][j-1], L0[i+1][j], L0[i+1][j+1])
        pixel1 = min(L1[i-1][j-1], L1[i-1][j], L1[i-1][j+1],
                     L1[i][j-1], L1[i][j+1],
                     L1[i+1][j-1], L1[i+1][j], L1[i+1][j+1])
        pixel2 = min(L2[i-1][j-1], L2[i-1][j], L2[i-1][j+1],
                     L2[i][j-1], L2[i][j], L2[i][j+1],
                     L2[i+1][j-1], L2[i+1][j], L2[i+1][j+1])
        pixelval = min(pixel0, pixel1, pixel2)
        if L1[i][j] >= Pixelval:
            keypoints.append([i,j])
        if L1[i][j] <= pixelval:
            keypoints.append([i,j])

#print(keypoints[1])
#print(keypoints[1][0])
for i in range(len(keypoints)):
    cv2.circle(imgcopy, (int(keypoints[i][1]), int(keypoints[i][0])), 1, (0, 0, 255), -1)

cv2.imwrite("Test/img/KeyPoints1sigma1_6.jpg", imgcopy)
        


    
    