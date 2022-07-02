#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 15:45:28 2022

@author: alessandrosebastianelli
"""

import numpy as np


def rgb_composite(image, rgb = [3,2,1]):
    '''
    
        Create an RGB composite.
                              (1c)
            
        Inputs:
            - image: must be a WxHxB MS image, with W width, H height and B bands, it must contain RGB bands
            - rgb: list of index correponing to RGB bands in image, must be a 3 element array
            
        Output:
            composite: a WxHx3 rgb image
    '''  
    
    composite = np.array([image[:,:,rgb[0]], image[:,:,rgb[1]], image[:,:,rgb[2]]])
    composite = np.moveaxis(composite, 0, -1)
    
    return composite

def swir_highlight(image, rgb = [3,2,1], swir = [10,11]):
    '''
    
        Create an RGB image in which pixels at high temperature are enanched.
        The formula is:
            
            RED   = a * RED   + max(0, SWIR1, 0.1)          (1a)
            GREEN = a * GREEN + max(0, SWIR2, 0.1)          (1b)
            BLUE  = a * BLUE                                (1c)
            
        Inputs:
            - image: must be a WxHxB MS image, with W width, H height and B bands, it must contain RGB and SWIR bands
            - rgb: list of index correponing to RGB bands in image, must be a 3 element array as in equation 1
            - swir: list of index correponing to swir bands in image, must be a 2 element array as in equation 1 
            
        Output:
            composite: a WxHx3 image with high temperature pixels higlighted
    '''    

    alpha = 2.5
    
    r = alpha * image[:,:,rgb[0]] + np.maximum(0, image[:,:,swir[0]] - 0.1)
    g = alpha * image[:,:,rgb[1]] + np.maximum(0, image[:,:,swir[1]] - 0.1)
    b = alpha * image[:,:,rgb[2]] 
    
    composite = np.array([r,g,b])
    composite = np.moveaxis(composite, 0, -1)
    
    return composite