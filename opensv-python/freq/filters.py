#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 14:58:11 2022

@author: alessandrosebastianelli
"""

import numpy as np

def gaussian_filter(fft, mx=0, my=0, sx=1, sy=1, invert=False):
    '''
    
        Apply a 2D gaussian filter to the input spectrum
        
        Inputs:
            - fft: 2D spectrum to be filtered
            - mx (my) (optional): mean
            - sx (sy) (optional): standard deviation
            - invert  (optional): invert the distribution
        Outputs:
            - filt: filtered spectrum
    '''
    
    x = np.linspace(-1, 1, fft.shape[0])
    y = np.linspace(-1, 1, fft.shape[1])
    
    x, y = np.meshgrid(x,y)

    fxy = 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))

    if invert: fxy = 1-fxy
    
    filt = fft*fxy
    
    return filt

def lhp_filter(fft, radius=0.5, invert=False):
    '''
    
        Apply a low pass or high pass filter to the input spectrum
        
        Inputs:
            - fft: 2D spectrum to be filtered
            - radius: size of the  filter [0-1]
            - invert  (optional): invert the distribution
        Outputs:
            - fft: filtered spectrum
    '''
    
    x = np.linspace(-1, 1, fft.shape[0])
    y = np.linspace(-1, 1, fft.shape[1])
    x, y = np.meshgrid(x, y)

    fxy = np.sqrt(x**2 + y**2)

    if invert: fxy = 1-fxy

    fft[fxy<radius] = 0
    
    return fft