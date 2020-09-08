#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 18:03:19 2020

@author: augustinjose
"""

from Descriptors.Descriptor import descriptors
from Resize.bilinear import Bilinear
from Transform.grayscale import Grayscale
from Transform.gaussian import GaussianBlurImage
from Difference.FilterDiff import filterDiff
from Homography.keypointMatcher import Matcher

import cv2
#import numpy.linalg as LA
#import numpy as np

def sift(img):
    imgcopy = cv2.imread("Input/test.jpg")
    s =1.3
    sigma = 1
    k = 2**(1/s)
    val = k * sigma
    octave = 4
    Pyramid = []

    img = Grayscale(img)
    height = img.shape[0]
    width = img.shape[1]
    layer = img
    gray = img
    for i in range(octave):
        layer = GaussianBlurImage(layer, val)
        #layer = cv2.GaussianBlur(layer,(5,5), val)
        #name = "Test/img/layer"+str(i)+".jpg"
        #cv2.imwrite(name, layer)
        Pyramid.append(layer)
    Diff = []
    for j in range(len(Pyramid)-1):
        diff = filterDiff(Pyramid[j+1], Pyramid[j])
        #Name = "Test/img/Interdiff"+str(j)+".jpg"
        #cv2.imwrite(Name, diff)
        Diff.append(diff)



    keypoints0 =[]
    keypoints1 =[]
    keypoints2 =[]
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
                         L0[i][j-1], L0[i][j+1],
                         L0[i+1][j-1], L0[i+1][j], L0[i+1][j+1])
            Pixel1 = max(L1[i-1][j-1], L1[i-1][j], L1[i-1][j+1],
                         L1[i][j-1], L1[i][j+1],
                         L1[i+1][j-1], L1[i+1][j], L1[i+1][j+1])
            Pixel2 = max(L2[i-1][j-1], L2[i-1][j], L2[i-1][j+1],
                         L2[i][j-1], L2[i][j], L2[i][j+1],
                         L2[i+1][j-1], L2[i+1][j], L2[i+1][j+1])

            pixel0 = min(L0[i-1][j-1], L0[i-1][j], L0[i-1][j+1],
                         L0[i][j-1], L0[i][j+1],
                         L0[i+1][j-1], L0[i+1][j], L0[i+1][j+1])
            pixel1 = min(L1[i-1][j-1], L1[i-1][j], L1[i-1][j+1],
                         L1[i][j-1], L1[i][j+1],
                         L1[i+1][j-1], L1[i+1][j], L1[i+1][j+1])
            pixel2 = min(L2[i-1][j-1], L2[i-1][j], L2[i-1][j+1],
                         L2[i][j-1], L2[i][j], L2[i][j+1],
                         L2[i+1][j-1], L2[i+1][j], L2[i+1][j+1])


            if L0[i][j] > Pixel0:
                keypoints0.append([i,j])
            if L0[i][j] < pixel0:
                keypoints0.append([i,j])
            if L1[i][j] > Pixel1:
                keypoints1.append([i,j])
            if L1[i][j] < pixel1:
                keypoints1.append([i,j])
            if L2[i][j] > Pixel2:
                keypoints2.append([i,j])
            if L2[i][j] < pixel2:
                keypoints2.append([i,j])

    #print(keypoints[1])
    #print(keypoints[1][0])
    imgcopy0 = imgcopy
    imgcopy1 = imgcopy
    imgcopy2 = imgcopy

    k_descriptors = descriptors(gray, keypoints0)
    #print(k_descriptors)
    '''
    for i in range(len(keypoints0)):
        cv2.circle(imgcopy0, (int(keypoints0[i][1]), int(keypoints0[i][0])), 1, (0, 0, 255), -1)

    for i in range(len(keypoints1)):
        cv2.circle(imgcopy1, (int(keypoints1[i][1]), int(keypoints1[i][0])), 1, (0, 0, 255), -1)
    for i in range(len(keypoints2)):
        cv2.circle(imgcopy2, (int(keypoints2[i][1]), int(keypoints2[i][0])), 1, (0, 0, 255), -1)


    cv2.imwrite("Test/img/LayerCheck0.jpg", imgcopy0)

    cv2.imwrite("Test/img/LayerCheck1.jpg", imgcopy1)
    cv2.imwrite("Test/img/LayerCheck2.jpg", imgcopy2)
    '''
    return k_descriptors
img1 = cv2.imread("Input/testleft.jpg")
img2 = cv2.imread("Input/testright.jpg")

k1 = sift(img1)
k2 = sift(img2)
f1, f2 = Matcher(k1,k2)
for i in range(len(f1)):
    cv2.circle(img1, (int(f1[i][1]), int(f1[i][0])), 1, (0, 0, 255), -1)
for i in range(len(f2)):
    cv2.circle(img2, (int(f2[i][1]), int(f2[i][0])), 1, (0, 0, 255), -1)
cv2.imwrite("Test/img/imgLeft.jpg", img1)
cv2.imwrite("Test/img/imgRight.jpg", img2)
