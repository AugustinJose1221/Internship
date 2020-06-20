#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 17:06:30 2020

@author: augustinjose
"""


import numpy as np

def Grayscale(img):
    img_height, img_width = img.shape[:2]
    #channel = img.shape[2]
    gray = np.empty([img_height, img_width])
    value = 0
    for i in range(img_height):
        for j in range(img_width):
            value = max(img[i][j][0], img[i][j][1], img[i][j][2])
            gray[i][j] = (value/255.0) * 100
    return gray
'''
import cv2
image = cv2.imread("../Test/img/test.jpg")
out = Grayscale(image)
cv2.imwrite("Output/gray1.jpg", out)
'''