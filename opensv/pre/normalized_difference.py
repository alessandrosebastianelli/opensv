#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:03:45 2022

@author: alessandrosebastianelli
"""

def normalized_difference(channel_1, channel_2):
    
    '''
        Normalized Difference
        
        nd = (channelA - channleB)/(channelA + channle_B + E)          (1)
        
        E is stabilizer term
        
        Inputs:
            - channel_1: channelA in equation (1)
            - channel_2: channelB in equation (1)
        
        Output:
            - nd: normalized difference between channelA and Channelb in equation (1)            
        
    '''
    
    num = channel_1 - channel_2
    den = channel_1 + channel_2
    
    # Avoiding 0 divisions
    den[den==0] = 0.001
    
    nd = num/den
    
    return nd