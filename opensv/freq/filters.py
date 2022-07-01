#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:58:11 2022

@author: alessandrosebastianelli
"""

import numpy as np

def gaussian_filter(shape, mx=0, my=0, sx=1, sy=1, invert=False):
    '''
    
        Create a 2D gaussian
        
        Inputs:
            - shape: dimension of the 2D gaussian
            - mx (my) (optional): mean
            - sx (sy) (optional): standard deviation
            - invert  (optional): invert the distribution
        Outputs:
            - fxy: 2D gaussian
    '''
    
    x = np.linspace(-1, 1, shape)
    y = np.linspace(-1, 1, shape)
    
    x, y = np.meshgrid(x,y)

    fxy = 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))

    if invert: fxy = 1-fxy
    
    return fxy