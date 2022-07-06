#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""

import sys

import numpy as np

sys.path.append('.')

from opensv.io.reader import load
from opensv.post.composite import rgb_composite
from opensv.pre.normalizer import max_scaler
from opensv.plot.cube import cube_plot
from opensv.utils.printer import print_stats


img, meta, bounds = load('tests/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-21.tif')
img = max_scaler(img, mmax = 10000)
rgb = 3*rgb_composite(img, rgb=[3, 2, 1])

expanded = np.repeat(img[:,:,:-3], 20, axis=-1)

print_stats(img, perband=False)
print_stats(img, perband=True)
#cube_plot(expanded)


























