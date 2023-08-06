#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:50:18 2022

@author: alessandrosebastianelli
"""

import numpy as np

def fft2d(image):
    '''
    
        Calculates the 2D Fast Fourier Transform of an image
        
        Input:
            - image: a WxH image, must be a single band image, with width W, height H
        Outputs:
            - fft: 2D spectrum of image
    '''
    
    fft = np.fft.fftshift(np.fft.fft2(image))
    
    return fft

def ifft2d(fft):
    '''
    
        Calculates the inverse 2D Fast Fourier Transform of a spectrum of an image
        
        Input:
            - fft: 2D spectrum of image 
        Outputs:
            - ifft: a WxH image
    '''
    
    ifft = np.abs(np.fft.ifft2(np.fft.ifftshift(fft)))
    
    return ifft
        
def fft3d(image):
    '''
    
        Calculates the 2D Fast Fourier Transform of an image with multiple bands
        
        Input:
            - image: a WxHxB image, with width W, height H and B bands
        Outputs:
            - fft: array of 2D spectra of the image
    '''
    
        
    ffts = []    
    for b in range(image.shape[-1]):
        ffts.append(fft2d(image[:,:,b]))
        
    ffts = np.array(ffts)
    ffts = np.moveaxis(ffts, 0, -1)
        
    return ffts 

def ifft3d(ffts):
    '''
    
        Calculates the inverse 2D Fast Fourier Transform of a vecctor of spectra of a multibands image
        
        Input:
            - fft: array of 2D spectra of the image
        Outputs:
            - ifft: a WxHxB image, with width W, height H and B bands
    '''
        
    iffts = []    
    for b in range(ffts.shape[-1]):
        iffts.append(ifft2d(ffts[:,:,b]))
        
    iffts = np.array(iffts)
    iffts = np.moveaxis(iffts, 0, -1)
        
    return iffts