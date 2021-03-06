#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:03:58 2020

@author: augustinjose
"""


import numpy as np

def filterDiff(img1, img2):
    img_height, img_width = img1.shape[:2]
    channel = 1#img1.shape[2]
    diff = np.empty([img_height, img_width, channel])
    pixel = 0
    for i in range(img_height):
        for j in range(img_width):
            for k in range(channel):
                pixel = img1[i][j] - img2[i][j]
                if pixel < 0:
                    pixel = 0
                diff[i][j][k] = pixel
                
    return diff
'''
import cv2 
img2 = cv2.imread("../Input/testgray11480.jpg")
img1 = cv2.imread("../Input/testgray12480.jpg")
out = filterDiff(img1, img2)
cv2.imwrite("Output/Testgray480Diff1.jpg", out)
'''
