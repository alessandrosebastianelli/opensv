#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 16:55:51 2022

@author: alessandrosebastianelli
"""

from setuptools import find_packages, setup

setup(
    name             = 'opensv',
    packages         = find_packages(include=['opensv']),
    version          = '0.0.1',
    description      = 'Open Satellite Vision',
    author           = 'Alessandro Sebastianelli',
    license          = 'MIT',
    install_requires = [
                       'numpy==1.21.2',
                       'matplotlib==3.4.3',
                       'rasterio==1.2.10',
                       'scipy==1.7.1',
                       'basemap==1.3.3'
                       ]
)