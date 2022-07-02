#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 16:52:56 2022

@author: alessandrosebastianelli
"""

import matplotlib.pyplot as plt

def plot(img, hist = False):
    
    ncols = 1
    if hist: ncols = 2
    
    fig, axes = plt.subplots(nrows = 1, ncols = ncols, figsize = (4*ncols, 4))

    if hist:
        axes[0].imshow(img)
        axes[0].set_title('Image')
        
        for b in range(img.shape[-1]):
            axes[1].hist(img[:,:,b].flatten(), 200, label='Band {}'.format(b))
        axes[1].legend()
        axes[1].set_title('Histogram')
    else:
        axes.imshow(img)
        axes.set_title('Image')
        
    fig.tight_layout()
    plt.show()



def bands_plot(img, hist = False): pass

    