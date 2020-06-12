#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:44:57 2020

@author: augustinjose
"""


import numpy as np

def transform(kernal):
    k = kernal.copy
    for i in range(kernal.shape[0]):
        for j in range(kernal.shape[1]):
            k[i][j] = kernal[kernal.shape[0]-i-1][kernal.shape[1]-j-1]
def Conv(image, kernal):
    kernal = transform(kernal)
    img_height = image.shape[0]
    img_width = image.shape[1]
    
    kernal_height = kernal.shape[0]
    kernal_width = kernal.shape[1]
    
    k_h = kernal_height // 2
    k_w = kernal_width // 2
    
    conv = np.zeros(image.shape)
    
    for i in range(k_h, img_height-k_h):
        for j in range(k_w, img_width-k_w):
            value = 0
            for x in range(kernal_height):
                for y in range(kernal_width):
                    value = value + kernal[x][y]*image[i-k_h+x][j-k_w+y]
            conv[i][j] = value
    
    return conv