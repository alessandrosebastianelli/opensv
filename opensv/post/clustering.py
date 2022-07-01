#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 19:42:46 2022

@author: alessandrosebastianelli
"""


from sklearn.cluster import KMeans
import numpy as np

def pixel_clustering(img, n_clusters = 3):
    '''
        Image pixel clustering using SVM
        
        Inputs:
            - img: a WxHxB image, with width W, height H and B bands
            - n_clusters: number of cluster to be identified
        Output:
            - cliusted: clustered pixels
    '''
    
    # For clustering the image using k-means, we first need to convert it into a 2-dimensional array
    image_2D = img.reshape(img.shape[0]*img.shape[1], img.shape[2])

    kmeans = KMeans(n_clusters = n_clusters, random_state = 0).fit(image_2D)
    #clustered = kmeans.cluster_centers_[kmeans.labels_]
    #clustered_3D = clustered.reshape(img.shape[0], img.shape[1], img.shape[2])
    
    cliusted = np.array(kmeans.labels_).reshape(img.shape[0], img.shape[1])
    
    return cliusted