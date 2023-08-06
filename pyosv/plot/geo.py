#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:13:29 2022

@author: alessandrosebastianelli
"""

from pyproj import Proj, transform
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import numpy as np


import ssl
ssl._create_default_https_context = ssl._create_unverified_context

  
    
def geo_plot(img, meta, bounds):

    
    inProj  = Proj('epsg:32632') # to fix - Leggere dai meta
    outProj = Proj('epsg:4326')
    
    row = bounds.top  + np.arange(img.shape[0])*meta['transform'][4]
    col = bounds.left + np.arange(img.shape[0])*meta['transform'][0]
    
    lat, lon = transform(inProj,outProj, col, row)    
    img_extent = [lon.min(), lon.max(), lat.min(), lat.max()]
    map_extent = [lon.min()-0.1, lon.max()+0.1, lat.min()-0.1, lat.max()+0.1]
    
    
    #------------ PLOT ------------
    ax = plt.axes(projection=ccrs.PlateCarree()) # Create map 
    ax.stock_img() # Put a BG
    
    # Plot img
    ax.imshow(img, origin='upper', alpha = 0.9, extent=img_extent, transform=ccrs.PlateCarree(), zorder = 100)
    
    # Add details
    ax.coastlines(resolution='50m', color='black', linewidth=1)
    ax.add_feature(cfeature.LAND)
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.LAKES)
    ax.add_feature(cfeature.RIVERS)
    ax.add_feature(cfeature.STATES)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.OCEAN)    
    ax.add_feature(cfeature.STATES)

        
    # Set limits
    ax.set_extent(map_extent)
    plt.show()


'''
def geo_plot_old(image, lat, lon):
    
    #m = Basemap(projection='merc', llcrnrlon=bounds[1], llcrnrlat=bounds[0],
    #            urcrnrlon=bounds[3], urcrnrlat=bounds[2], resolution='h')
    
    m = Basemap(projection='merc',
        llcrnrlon=lon.min(), llcrnrlat=lat.min(),
        urcrnrlon=lon.max(), urcrnrlat=lat.max(), 
        resolution="h")
    
    #m.drawcountries() 
    
    #m.drawstates()
    
    
    #extent = [bounds[1], bounds[0], bounds[3], bounds[2]]
    
    #print(image[:,:-3,0].min(), image[:,:-3,0].max(), image[:,:-3,0].mean())
    
    #m.contourf(lat, lon, image[:,:-3,0].squeeze(), levels = np.linspace(0,5,100))
    m.imshow(image, extent = [lon.min(),lat.min(), lon.min(), lon.max() ], alpha=0.6, aspect='auto', origin='upper')
    #m.drawcoastlines()
    m.drawcoastlines()
    #m.drawmeridians()
    #m.drawparallels()
    
    plt.show()
  ''' 

    
