#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 7 16:16:42 2022

@author: alessandrosebastianelli
"""

import numpy as np

def patch_extractor(image, shape=(64, 64), stride=(1, 1)):
    '''

        Extracts patches of 'shape' from 'image' with 'stride'

        Inputs:
            - image: a WxHxB image, with width W, height H and B bands
            - shape (optional): shape of the patches
            - stride (optional): stride of the moving window
        Output:
            - patches: a Pxshape(0)xshape(1)xB set of images, with P patches of width shape(0), height shape(1) and B bands
    '''

    width, height, channels = image.shape
    w_out = 1 + ((width - shape[0]) // stride[0])
    h_out = 1 + ((height - shape[1]) // stride[1])
    patches = np.zeros((w_out * h_out, shape[0], shape[1], channels))

    ct = 0
    for j in range(0, height - shape[1], stride[1]):
        for i in range(0, width - shape[0], stride[0]):
            patches[ct, :, :, :] = image[j:j + shape[1], i:i + shape[0], :]

            ct += 1

    return patches


def patch_iterator(image, shape=(64, 64), stride=(1, 1)):
    '''

        (Iterator) Extracts patches of 'shape' from 'image' with 'stride'

        Inputs:
            - image: a WxHxB image, with width W, height H and B bands
            - shape (optional): shape of the patches
            - stride (optional): stride of the moving window
        Output:
            - patch: a shape(0)xshape(1)xB patch of width shape(0), height shape(1) and B bands
    '''

    width, height, channels = image.shape

    w_out = 1 + ((width - shape[0]) // stride[0])
    h_out = 1 + ((height - shape[1]) // stride[1])

    for j in range(0, height - shape[1], stride[1]):
        for i in range(0, width - shape[0], stride[0]):
            yield image[j:j + shape[1], i:i + shape[0], :]
