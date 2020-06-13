#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 12:20:31 2020

@author: augustinjose
"""


import math
import numpy as np

def Bilinear(image, height, width):
  """
  `image` is a 2-D numpy array
  `height` and `width` are the desired spatial dimension of the new 2-D array.
  """
  img_height, img_width = image.shape[:2]
  channel = image.shape[2]
  resized = np.empty([height, width, channel])
  
  x_ratio = float(img_width - 1) / (width - 1) if width > 1 else 0
  y_ratio = float(img_height - 1) / (height - 1) if height > 1 else 0

  for i in range(height):
    for j in range(width):
        for k in range(channel):
          x_l, y_l = math.floor(x_ratio * j), math.floor(y_ratio * i)
          x_h, y_h = math.ceil(x_ratio * j), math.ceil(y_ratio * i)
    
          x_weight = (x_ratio * j) - x_l
          y_weight = (y_ratio * i) - y_l
    
          a = image[y_l, x_l, k]
          b = image[y_l, x_h, k]
          c = image[y_h, x_l, k]
          d = image[y_h, x_h, k]
    
          pixel = a * (1 - x_weight) * (1 - y_weight)  + b * x_weight * (1 - y_weight) + c * y_weight * (1 - x_weight) + d * x_weight * y_weight
          resized[i][j][k] = pixel

  return resized