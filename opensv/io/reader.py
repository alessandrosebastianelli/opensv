#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 19:55:06 2022

@author: alessandrosebastianelli
"""

from ..utils.paths import get_path_gui


import matplotlib.pyplot as plt
import numpy as np
import rasterio


def load(path):
    '''
    
        Load an image and its metadata given its path
        
        Inputs:
            - path: position of the image, if None the function will ask for the image path using a menu
            - info (optional): allows to print process informations
        Outputs:
            - data: WxHxB image, with W width, H height and B bands
            - metadata: dictionary containing image metadata
    '''
    
    
    RASTERIO_EXTENSIONS   = ['.tif', '.tiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg']
    
    
    if path is None:
        path = get_path_gui()
    
    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):
        
        with rasterio.open(path) as src:
            
            data = src.read()
            metadata = src.profile
            bounds = src.bounds
                        
        data = np.moveaxis(data, 0, -1)
        
    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        
        data = plt.imread(path)
        metadata = None
        bounds = None
        
    else:
        
        data = None
        metadata = None
        bounds = None
        print('[!] File can not be opened, format not supported!')
        
    return data, metadata, bounds