#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 5 14:01:04 2022

@author: alessandrosebastianelli
"""


import matplotlib.pyplot as plt
import numpy as np


def cube_plot(image):
    '''
        3D - Plot of a multibands image.

        !!! This function is not efficient, so use it carefully.
        A 64x64x12 image takes minutes to be rendered!!!

        Input:
            - image: a WxHxB image, with height H, width W and B bands

    '''

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    colors = np.repeat(image[:, :, :, np.newaxis], 3, axis=3)
    ax.voxels(image, facecolors=colors, edgecolors=None)
    ax.axis(False)
    plt.show()



