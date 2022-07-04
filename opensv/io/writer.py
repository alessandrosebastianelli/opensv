#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:49:04 2022

@author: alessandrosebastianelli
"""


def save(image, path):

    RASTERIO_EXTENSIONS   = ['.tif', '.tiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg']

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):
        # To be implemented, save as tiff
        pass

    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        plt.imsave(path, image)

    else:
        print('[!] File can not be saved, format not supported!')