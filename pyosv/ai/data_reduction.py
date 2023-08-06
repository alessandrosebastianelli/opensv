#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 7 10:56:04 2022

@author: alessandrosebastianelli
"""

from sklearn.decomposition import PCA

def image_PCA(image, n_components):
    '''

        Reduce the image dimensionality along the frequency axis using PLA

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


def image_stack_PCA(images, n_components):
    '''

        !!!To be implemented!!!

        Reduce a temporal stack of images along the temporal axis

        Inputs:
            - images: a TxWxHxB stack of images, with T temporal length, width W, height H and B bands
            - n_components: number of bands of the compressed image
        Output:
            - reduced: the n_componentsxWxHxB compressed image, n_components temporal length, with width W, height H and B bands

    '''

    pass