#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:40:15 2022

@author: alessandrosebastianelli
"""


from tkinter.filedialog import askopenfilename
from tkinter import Tk


def get_path_gui():
    
    '''
        Get the path of a file using a graphical menu    
        
        Output:
            - path: path of the image
    '''
    
    root = Tk()
    root.withdraw()
    path = askopenfilename(
        title='Select the image to read!',
        initialdir='/'
        )
    root.destroy()
    
    return path