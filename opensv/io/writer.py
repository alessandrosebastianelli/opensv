#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:49:04 2022

@author: alessandrosebastianelli
"""


def save(image, path, srcimage=None):
    '''

        Save an image and its metadata given its path

        Inputs:
            - image: the image to be saved
            - path: position of the image
            - srcimage (optional): source image, used to copy metdata and CRS, must be a rasterio object
    '''

    RASTERIO_EXTENSIONS   = ['.tif', '.tiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg']

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):

        if srcimage!=None:
            meta = srcimage.meta.copy()
            meta.update({'driver':'GTiff',
                            'width':image.shape[0],
                            'height':image.shape[1],
                            'count':image.shape[2],
                            'dtype':'float64',
                            'crs':srcimage.crs, 
                            'transform':srcimage.transform,
                            'nodata':0})

        with rasterio.open(fp=path, mode='w',**out_meta) as dst:
            for count in range(image.shape[2]):
                dst.write(image[:,:,count], count)

    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        plt.imsave(path, image)

    else:
        print('[!] File can not be saved, format not supported!')