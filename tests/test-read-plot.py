#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""

from opensv.io.reader import load
from opensv.post.composite import rgb_composite
from opensv.pre.normalizer import max_scaler

import matplotlib.pyplot as plt
import numpy as np

img, meta, bounds = load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')

#load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-21.tif')

#load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')
img = max_scaler(img, mmax = 4000)

rgb = rgb_composite(img, rgb=[3,2,1])
rgb = np.clip(rgb, 0.0, 1.0)






fig, axes = plt.subplots(nrows = 2, ncols = 1, figsize = (6,8))

axes[0].imshow(rgb)

fig.tight_layout()
plt.show()






















