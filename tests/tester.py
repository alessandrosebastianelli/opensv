#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""

import sys
sys.path.append('.')

import numpy as np

from opensv.io.batch_reader import load

from opensv.post.composite import rgb_composite
from opensv.pre.normalizer import max_scaler
from opensv.plot.cube import cube_plot


img, meta, bounds = load('tests/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-21.tif', shape=256)


























