#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:47:42 2022

@author: alessandrosebastianelli
"""
        
from opensv.io.reader import load
from opensv.post.composite import rgb_composite
from opensv.pre.normalizer import max_scaler
from opensv.plot.plot import plot, bands_plot



img, meta, bounds = load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')

#load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-21.tif')

#load('/Users/alessandrosebastianelli/Desktop/SentinelDataAnalysis/data/S2-lat_45_85299971127813_lon_10_852932810361423-2019-06-13_2.tif')
img = max_scaler(img, mmax = 10000)
rgb = 3*rgb_composite(img, rgb=[3,2,1])


bands_plot(img, hist=False)























