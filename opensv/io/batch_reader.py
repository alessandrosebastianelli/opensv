#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:28:06 2022

@author: alessandrosebastianelli
"""

from ..utils.paths import get_path_gui

from rasterio.windows import Window
import matplotlib.pyplot as plt
from tqdm import tqdm
import numpy as np
import rasterio


def load(path, shape=256):
    '''

        Load an image and its metadata given its path

        Inputs:
            - path: position of the image, if None the function will ask for the image path using a menu
        Outputs:
            - data: WxHxB image, with W width, H height and B bands
            - metadata: dictionary containing image metadata
    '''

    RASTERIO_EXTENSIONS = ['.tif', '.tiff']

    if path is None:
        path = get_path_gui()

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):

        with rasterio.open(path) as src:
            #data = src.read()
            w, h = src.width, src.height
            metadata = src.profile
            bounds = src.bounds

        out = np.zeros((w, h, 3))

        for i in tqdm(range(0, w - shape, shape)):
            for j in range(0, h - shape, shape):
                with rasterio.open(path) as src:
                    data = src.read(window=Window(j, i, shape, shape))
                    data = np.moveaxis(data, 0, -1)/10000
                    out[i:i + 256, j:j + 256, 0] = data[:, :, 4]
                    out[i:i + 256, j:j + 256, 1] = data[:, :, 3]
                    out[i:i + 256, j:j + 256, 2] = data[:, :, 2]

        fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(50, 50))
        ax.imshow(out)
        ax.axis(False)
        plt.show()

        p = path.split('.')[0] + '.png'
        print(p)
        plt.savefig(p)

        plt.close()


    else:
        data = None
        metadata = None
        bounds = None
        print('[!] File can not be opened, format not supported!')

    return data, metadata, bounds