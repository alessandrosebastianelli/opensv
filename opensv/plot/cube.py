#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 5 14:01:04 2022

@author: alessandrosebastianelli
"""


import matplotlib.pyplot as plt
import numpy as np


def cube_plot(image):

    fig = plt.figure()

    ax = fig.gca(projection='3d')

    colors = np.repeat(image[:, :, :, np.newaxis], 3, axis=3)

    ax.voxels(image, facecolors=colors, edgecolors=None)

    ax.axis(False)
    plt.show()

