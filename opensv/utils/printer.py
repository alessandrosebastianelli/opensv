#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 20:19:40 2022

@author: alessandrosebastianelli
"""

def dict_disp(dict):

    print('//----------- Dictionary -----------//')

    for key, value in dict.items():
        print('\t [*] {} : {}'.format(key, value))
        