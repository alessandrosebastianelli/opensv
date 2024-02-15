from ..utils.paths import get_path_gui

import matplotlib.pyplot as plt
import numpy as np
import rasterio
import netCDF4


def write(image : np.ndarray, path : str, meta : dict) -> None:
    '''
        Save an image and its metadata given a path.

        Supported data format

        RASTERIO_EXTENSIONS   = ['.tif', '.tiff', '.geotiff']  
        MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg', 'jp2']
        NETCDF4_EXTENSIONS    = ['.nc']

        Data must always be in channel last format.

        If image extension is in MATPLOTLIB_EXTENSIONS, metadata can be None.
        If image extension is in NETCDF4_EXTENSIONS, metadata can be None.

        Parameters:
        -----------
            - image : np.ndarray
                the WxHxC image to be saved, with W width, H height and B bands (channel last)
            - path : str 
                position of the image, if None the function will ask for the image path using a menu
            - meta : dict
                metadata for the image to be saved
        
        Returns:
        --------
        Nothing, the image will be saved

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
                [1.1, 1.2, 1.3],  
                [1.4, 1.5, 1.6],  
                [1.7, 1.8, 1.9]
             ]
            ]  
        ) 

        # Making channels last
        img = np.moveaxis(img, 0, -1)

        write(img, 'path/to/save/img.png')
        
        ```
        Output:
        -------
        Nothing, the image will be saved


    '''

    RASTERIO_EXTENSIONS   = ['.tif', '.tiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg', 'jp2']
    NETCDF4_EXTENSIONS    = ['.nc']


    if path is None:
        path = get_path_gui()

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):
        if image!=None:
            meta.update({'driver':'GTiff',
                            'width':image.shape[0],
                            'height':image.shape[1],
                            'count':image.shape[2],
                            'dtype':'float64'})

        with rasterio.open(fp=path, mode='w',**meta) as dst:
            for count in range(image.shape[2]):
                dst.write(image[:,:,count], count)

    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        plt.imsave(path, image)
    elif any(frmt in path for frmt in NETCDF4_EXTENSIONS):
        raise Exception('Error: [under dev] currently netCDF4 files can not be saved!')
    else:
        raise Exception('Error: file can not be saved, format not supported!')
