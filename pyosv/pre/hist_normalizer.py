#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 16:07:47 2022

@author: alessandrosebastianelli
"""

from ..utils.mapper import mapFromTo


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, mainloop, Scale, HORIZONTAL
import matplotlib.pyplot as plt
import numpy as np


def hist_normalizer(img):
    '''
    
        Open a gui that helps to stretch the histogram of an image
    
        
        Inputs:
            - img: a WxHxB image, with width W, height H and B bands (B can be 1 or 3) 
    '''
    
    # Update plot
    def plot(img):
        # Clear axis
        axes[0].cla()
        axes[1].cla()
        
        # Plot image and histogram
        axes[0].set_title('Image')
        img = mapFromTo(img, wmin.get(), wmax.get(), 0, 1)
        axes[0].imshow(img)
    
        axes[1].set_title('Histogram')
        axes[1].set_xlabel('Mapped Pixel Values')
        axes[1].set_ylabel('Frequency')
    
        for k in range(img.shape[-1]):
            axes[1].hist(img[:,:,k].flatten(), 200, label = 'Band-{}'.format(k))   
            
        axes[1].legend()
        chart_type.draw()
    
    # Scale values using the sliders
    def scalevalue(value, other = img):
        image = np.clip(img, wmin.get(), wmax.get())    
        plot(image)
    
    figure, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(10,5), dpi=100)
    
    # GUI
    root = Tk()
    root.title('Histrogram Scaler')
    root.geometry('1000x620')
    root.resizable(False, False)
    
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()
    
    wmin = Scale(root, from_=np.min(img), to=np.max(img), length = 400, label='Minimum', orient=HORIZONTAL, command = scalevalue)
    wmin.set(np.min(img))
    wmin.pack()
    wmax = Scale(root, from_=np.min(img), to=np.max(img), length = 400, label='Maximum', orient=HORIZONTAL, command = scalevalue)
    wmax.set(np.max(img))
    wmax.pack()
    
    mainloop()