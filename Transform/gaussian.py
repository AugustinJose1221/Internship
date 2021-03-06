#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:02:47 2020

@author: augustinjose
"""


import numpy as np
from PIL import Image
import cv2
def convolution(oldimage, kernel):
    #image = Image.fromarray(image, 'RGB')
    image_h = oldimage.shape[0]
    image_w = oldimage.shape[1]
    #print(image_h)
    
    kernel_h = kernel.shape[0]
    kernel_w = kernel.shape[1]
    #print(kernel_h)
    if(len(oldimage.shape) == 3):
        image_pad = np.pad(oldimage, pad_width=((kernel_h // 2, kernel_h // 2),(kernel_w // 2, kernel_w // 2),(0,0)), mode='constant', constant_values=0).astype(np.float32)    
    elif(len(oldimage.shape) == 2):
        image_pad = np.pad(oldimage, pad_width=((kernel_h // 2, kernel_h // 2),(kernel_w // 2, kernel_w // 2)), mode='constant', constant_values=0).astype(np.float32)
    
    
    h = kernel_h // 2
    w = kernel_w // 2
    
    image_conv = np.zeros(image_pad.shape)
    
    for i in range(h, image_pad.shape[0]-h):
        for j in range(w, image_pad.shape[1]-w):
            #sum = 0
            x = image_pad[i-h:i-h+kernel_h, j-w:j-w+kernel_w]
            x = x.flatten()*kernel.flatten()
            image_conv[i][j] = x.sum()
    h_end = -h
    w_end = -w
    
    if(h == 0):
        return image_conv[h:,w:w_end]
    if(w == 0):
        return image_conv[h:h_end,w:]
    return image_conv[h:h_end,w:w_end]
    
def GaussianBlurImage(image, sigma):
    #image = cv2.imread(image)
    #image = Image.open(image)
    #image = np.asarray(image)
    #print(image)
    filter_size = 2 * int(4 * sigma + 0.5) + 1
    gaussian_filter = np.zeros((filter_size, filter_size), np.float32)
    m = filter_size//2
    n = filter_size//2
    
    for x in range(-m, m+1):
        for y in range(-n, n+1):
            x1 = 2*np.pi*(sigma**2)
            x2 = np.exp(-(x**2 + y**2)/(2* sigma**2))
            gaussian_filter[x+m, y+n] = (1/x1)*x2
    im_filtered = np.zeros_like(image, dtype=np.float32)
    '''
    gaussian_filter = np.array([[0.00390625,0.015625,0.0234375,0.015625,0.00390625],
                                [0.015625,0.0625,0.09375,0.0625,0.015625],
                                [0.0234375,0.09375,0.140625,0.09375,0.0234375],
                                [0.015625,0.0625,0.09375,0.0625,0.015625],
                                [0.00390625,0.015625,0.0234375,0.015625,0.00390625]])
    '''
    im_filtered[:, :] = convolution(image[:, :], gaussian_filter)  
    #for c in range(3):
        #im_filtered[:, :, c] = convolution(image[:, :, c], gaussian_filter)  
        #print(gaussian_filter)
    return (im_filtered.astype(np.uint8))
'''
image = GaussianBlurImage("img/test480gray1.jpg", 12)
img = Image.fromarray(image, 'L')
img.save('Output/testgray12480.jpg')
img.show()
'''