#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 10:52:26 2022

@author: alessandrosebastianelli
"""

from ..pre.normalized_difference import normalized_difference


def ndvi(image, red_index=3, nir_index=7):
    '''
        Calculate the Normalized Difference Vegetation Index described by equation (1)
        
        NDVI = (NIR-RED)/(NIR+RED)          (1)
        
        where NIR and RED are the near infrared and red bands
        
        
        Inputs:
            - image: a WxHxB MS image, with W width, H height and B bands            
            - red_index (default 3 for Sentinel-2): is the index of the RED band in image
            - nir_index (default 7 for Sentinel-2): is the index of the NIR band in image
        Outputs:
            - ndvi: the NDVI calculated using (1)

    '''

    ndvi_v = normalized_difference(image[:, :, nir_index], image[:, :, red_index])

    return ndvi_v
