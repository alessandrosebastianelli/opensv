#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 5 14:01:04 2022

@author: alessandrosebastianelli
"""

from mayavi import mlab

def plot3d(image, animate = False):
    '''
        3D-Plot of a multibands image.

        Input:
            - image: a WxHxB image, with height H, width W and B bands
            - animate: activate the animation mode

    '''

    fig = mlab.figure(figure='Plot 3D', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(600, 600))

    v = mlab.volume_slice(image, slice_index=0, plane_orientation='z_axes', figure=fig)  # depth slice

    if animate:
        @mlab.animate
        def anim():
            ct = 0
            while True:
                if ct >= image.shape[-1]:
                    ct = 0
                v.mlab_source.scalars = image[:, :, ct]
                ct += 1

                yield
        anim()

    mlab.show()

def cube_plot(image):
    '''
        Plot data cube

        Input:
            - image: a WxHxB image, with height H, width W and B bands

    '''

    fig = mlab.figure(figure='Cube Plot', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(600, 600))

    scalars = image  # specifying the data array

    # Crossline slices
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='x_axes', figure=fig)  # crossline slice
    mlab.volume_slice(scalars, slice_index=image.shape[0], plane_orientation='x_axes', figure=fig)  # crossline slice

    # Inline slices
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='y_axes', figure=fig)  # inline slice
    mlab.volume_slice(scalars, slice_index=image.shape[1], plane_orientation='y_axes', figure=fig)  # inline slice
    # Dept slices

    mlab.volume_slice(scalars, slice_index=image.shape[-1], plane_orientation='z_axes', figure=fig)  # depth slice
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='z_axes', figure=fig)  # depth slice

    mlab.draw()
    mlab.show()