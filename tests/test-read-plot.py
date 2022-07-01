#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""



from opensv.io.reader import load
from opensv.pre.normalizer import minmax_scaler

from opensv.plot.geo_plot import geo_plot

import numpy as np

img, meta, bounds = load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')
img = minmax_scaler(img, clip=[0,1])

rgb = 5*np.array(
    [
     img[:,:,3],
     img[:,:,2],
     img[:,:,1]
     ]
    )

rgb = np.moveaxis(rgb, 0, -1)

geo_plot(rgb, meta, bounds)
























