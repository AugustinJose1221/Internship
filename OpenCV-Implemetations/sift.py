#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 14:02:57 2020

@author: augustinjose
"""

import cv2
import numpy as np

img = cv2.imread('../Input/test.jpg')
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
sift = cv2.SIFT()
kp = sift.detect(gray,None)
'''
descriptor = cv2.xfeatures2d.SIFT_create()
(kps, features) = descriptor.detectAndCompute(gray, None)
img=cv2.drawKeypoints(gray,kps, outImage = None)

cv2.imwrite('output/sift-test3.jpg',img)