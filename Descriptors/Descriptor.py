#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:46:52 2020

@author: augustinjose
"""


import numpy as np

def descriptors(img, keypoints):
    img_height = img.shape[0]
    img_width = img.shape[1]
    window = []
    for i in keypoints:
        x = int(keypoints[1])
        y = int(keypoints[0])
        x_new = x-8
        y_new= y-8
        if x <= 9 or y <= 9:
            continue
        if img_width-x <= 9 or img_height-y <=9:
            continue
        else:
            for j in range(16):
                for k in range(16):
                    dx=img[x_new+j+1][y_new+k]-img[x_new+j-1][y_new+k]
                    dy=img[x_new+j][y_new+k+1]-img[x_new+j][y_new+k-1]
                    window[i][j]=[((dx*dx)+(dy*dy))**0.5, dy/dx]
                
                
            