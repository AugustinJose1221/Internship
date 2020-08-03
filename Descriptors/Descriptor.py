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
    descriptor = []
    for i in range(len(keypoints)):
        x = int(keypoints[i][1])
        y = int(keypoints[i][0])
        x_new = x-8
        y_new= y-8
        if x <= 9 or y <= 9:
            continue
        if img_width-x <= 9 or img_height-y <=9:
            continue
        else:
            window = np.empty([16,16,2])
            for j in range(16):
                for k in range(16):
                    dx=int(img[x_new+j+1][y_new+k]) - int(img[x_new+j-1][y_new+k])
                    if dx==0:
                        dx=0.01
                    dy=int(img[x_new+j][y_new+k+1]) - int(img[x_new+j][y_new+k-1])
                    window[j][k] = [((dx*dx)+(dy*dy))**0.5, dy/dx]
            desc=np.empty([4,4,2])
            for j in range(4):
                for k in range(4):
                    desc[j][k] = grad(window[j*4:(j*4)+4][k*4:(k*4)+4][:])
            D=[0,0,0,0]
            for j in range(4):
                for k in range(4):
                    if desc[j][k][1]<=1 and desc[j][k][1]>=0:
                        D[0] = D[0] + desc[j][k][0]
                    elif desc[j][k][1]>1:
                        D[1] = D[1] + desc[j][k][0]
                    elif desc[j][k][1]<-1:
                        D[2] = D[2] + desc[j][k][0]
                    elif desc[j][k][1]>=-1 and desc[j][k][1]<0:
                        D[3] = D[3] + desc[j][k][0]
        descriptor.append(D)
    return descriptor

def grad(array):
    print(array.shape[0])
    print(array.shape[1])
    print(array.shape[2])
    #print(array)
    flat = []
    for j in range(4):
        for k in range(4):
            flat.append(array[j][k][0])
    grad = max(flat)
    for i in range(len(flat)):
        if flat[i]==grad:
            pos=i
            break
    x = int(pos/4)
    y = pos%4
    return [grad, array[x][y][1]]

            