#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""

from opensv.io.reader import load
from opensv.post.clouds import cloud_detector, white_detector
from opensv.pre.normalizer import max_scaler

import matplotlib.pyplot as plt
import numpy as np

img, meta, bounds = load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-21.tif')

#load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')
img = max_scaler(img, mmax = 4000)


rgb = np.array(
    [
     img[:,:,3],
     img[:,:,2],
     img[:,:,1]
     ]
    )

rgb = np.moveaxis(rgb, 0, -1)
score = cloud_detector(img, cloud_threshold=0.1)
score2 = white_detector(rgb, cloud_threshold=0.8)


fig, axes = plt.subplots(nrows = 1, ncols = 2, figsize = (10,5))
axes[0].imshow(rgb)
axes[1].imshow((score+score2)/2)
plt.show()
























