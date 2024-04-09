from mayavi import mlab
import numpy as np

def plot3d(img : np.ndarray, animate : bool = False) -> None:
    '''
        3D-Plot of a satellite image.

        Parameters:
        ----------
            - img : np.ndarray
                a WxHxB image, with width W, height H and B bands (B can be 3 or 1)
            - animate : bool
                activate animation mode (dafault : False)
        
        Returns:
        --------
        Nothing, it will display the image

        Usage:
        ------

        ```python
        import numpy as np

        img         = np.array(  
            [[
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
             ],
             [
                [0.9, 0.8, 0.7],  
                [0.6, 0.5, 0.4],  
                [0.3, 0.2, 0.1]
             ]
            ]  
        ) 

        # Making channel last
        img = np.moveaxis(img, 0, -1)

        plot3d(img, animate=True)

        ```

        Output:
        -------
        Nothing, it will display the image

    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')

    fig = mlab.figure(figure='', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(600, 600))
    v = mlab.volume_slice(img, slice_index=0, plane_orientation='z_axes', figure=fig)  # depth slice

    if animate:
        @mlab.animate
        def anim():
            ct = 0
            while True:
                if ct >= img.shape[-1]:
                    ct = 0
                v.mlab_source.scalars = img[:, :, ct]
                ct += 1
                yield
        anim()
    mlab.show()


def cube_plot(img : np.ndarray, save_path : str, band_thinkness : int = 3, cmap : str = 'jet', show : bool = True) -> None:
    '''
        Cube pot of a satellite image.

        Parameters:
        ----------
            - img : np.ndarray
                a WxHxB image, with width W, height H and B bands (B can be 3 or 1)
            - save_path : str
                path where to save figure
            - band_thinkness : int
                thikness of each satellite band
            - cmap : str
                colormap for the plot
            - show : bool
                if True will show the plot, othewise will be only saved to a file
        
        Returns:
        --------
        Nothing, it will display the image

        Usage:
        ------

        ```python
        import numpy as np

        img         = np.array(  
            [[
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
             ],
             [
                [0.9, 0.8, 0.7],  
                [0.6, 0.5, 0.4],  
                [0.3, 0.2, 0.1]
             ]
            ]  
        ) 

        # Making channel last
        img = np.moveaxis(img, 0, -1)

        cube_plot(img, 'img.png', band_thikness=10, cmap='jet', show=True)

        ```

        Output:
        -------
        Nothing, it will display the image

    '''
    
    if len(img.shape) != 3: raise Exception("Error: lenght of img shape must be 3")


    img = np.repeat(img, band_thinkness, axis=-1)

    fig = mlab.figure(figure='', bgcolor=(1, 1, 1), fgcolor=(0, 0, 0), size=(600, 600))

    scalars = img  # specifying the data array

    # Crossline slices
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='x_axes', figure=fig, colormap=cmap)  # crossline slice
    mlab.volume_slice(scalars, slice_index=img.shape[0], plane_orientation='x_axes', figure=fig, colormap=cmap)  # crossline slice

    # Inline slices
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='y_axes', figure=fig, colormap=cmap)  # inline slice
    mlab.volume_slice(scalars, slice_index=img.shape[1], plane_orientation='y_axes', figure=fig, colormap=cmap)  # inline slice

    # Depth slices
    mlab.volume_slice(scalars, slice_index=img.shape[-1], plane_orientation='z_axes', figure=fig, colormap=cmap)  # depth slice
    mlab.volume_slice(scalars, slice_index=0, plane_orientation='z_axes', figure=fig, colormap=cmap)  # depth slice


    mlab.draw()

    mlab.savefig(filename=save_path)

    if show: mlab.show()