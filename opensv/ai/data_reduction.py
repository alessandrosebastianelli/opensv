#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 7 10:56:04 2022

@author: alessandrosebastianelli
"""

from sklearn.decomposition import PCA


def image_PCA(image, n_components=3):
    '''
        Reduce the image dimensionality along the frequency axis

        Inputs:
            - image: a WxHxB image, with width W, height H and B bands
            - n_components: number of bands of the compressed image
        Output:
            - reduced: the WxHxn_components compressed image, with width W, height H and n_components bands
    '''

    pca = PCA(n_components)
    reduced = pca.fit_transform(image.reshape((image.shape[0] * image.shape[1], image.shape[2])))
    reduced = reduced.reshape((image.shape[0], image.shape[1], n_components))

    return reduced
