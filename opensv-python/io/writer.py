#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:49:04 2022

@author: alessandrosebastianelli
"""

import matplotlib.pyplot as plt
import rasterio


def save(image, path, meta):
    '''

        Save an image and its metadata given its path

        Inputs:
            - image: the image to be saved
            - path: position of the image
            - meta: metadata for the image to be saved
    '''

    RASTERIO_EXTENSIONS   = ['.tif', '.tiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg']

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):

        if image!=None:
            meta.update({'driver':'GTiff',
                            'width':image.shape[0],
                            'height':image.shape[1],
                            'count':image.shape[2],
                            'dtype':'float64'})

        with rasterio.open(fp=path, mode='w',**meta) as dst:
            for count in range(image.shape[2]):
                dst.write(image[:,:,count], count)

    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        plt.imsave(path, image)

    else:
        print('[!] File can not be saved, format not supported!')