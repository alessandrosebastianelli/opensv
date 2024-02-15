from ..utils.paths import get_path_gui

import matplotlib.pyplot as plt
import numpy as np
import rasterio
import netCDF4


def load(path : str) -> [np.ndarray or dict, dict, list]:
    '''
        Load an image and its metadata given its path.

        Supported data format

        RASTERIO_EXTENSIONS   = ['.tif', '.tiff', '.geotiff']  
        MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg', 'jp2']
        NETCDF4_EXTENSIONS    = ['.nc']

        Returns always data in channel last format.

        If image extension is in MATPLOTLIB_EXTENSIONS, metadata and bouns will be None.
        If image extension is in NETCDF4_EXTENSIONS, metadata and bounds will be None.
        
        Parameters:
        -----------
            - path : str
                position of the image, if None the function will ask for the image path using a menu

        Returns:
        --------
            - data : np.ndarray or list
                WxHxB image, with W width, H height and B bands

            - metadata : dict
                dictionary containing image metadata
            
            - bounds : list
                list containing geo bounds
        
        Usage:
        ------
        ```python
            img = load(None)
        ``` 
        or
        ```python
            img = load("path/to/image.png")
        ``` 

        Output:
        -------
        ```
        (
            array([[[5872., 5532., 5516., ...,    0.,    0., 1024.],  
                    [5872., 5588., 5451., ...,    0.,    0., 1024.],  
                    [5872., 5606., 5333., ...,    0.,    0., 1024.],  
                    ...,  
                    [2672., 2602., 2368., ...,    0.,    0., 1024.],  
                    [2672., 2689., 2394., ...,    0.,    0., 1024.],  
                    [2672., 2705., 2431., ...,    0.,    0., 1024.]],  
                    ...,  
                    [[1571., 1318., 1167., ...,    0.,    0.,    0.],  
                    [1571., 1206., 1113., ...,    0.,    0.,    0.],  
                    [1571., 1230., 1094., ...,    0.,    0.,    0.],  
                    ...,  
                    [1330., 1044.,  837., ...,    0.,    0.,    0.],  
                    [1330., 1045.,  842., ...,    0.,    0.,    0.],  
                    [1330., 1032.,  833., ...,    0.,    0.,    0.]]]),  
            
            {'driver': 'GTiff', 'dtype': 'float64', 'nodata': None, 'width': 1043, 'height': 1040, 'count': 16, 'crs': CRS.from_epsg(32632), 'transform': Affine(10.0, 0.0, 638640.0,
       0.0, -10.0, 5084590.0), 'blockxsize': 256, 'blockysize': 256, 'tiled': True, 'compress': 'lzw', 'interleave': 'pixel'},  

       BoundingBox(left=638640.0, bottom=5074190.0, right=649070.0, top=5084590.0))  
        )

        ```
    '''
    
    
    RASTERIO_EXTENSIONS   = ['.tif', '.tiff', '.geotiff']
    MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg', 'jp2']
    NETCDF4_EXTENSIONS    = ['.nc']
    
    
    if path is None:
        path = get_path_gui()
    
    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):
        with rasterio.open(path) as src:
            data = src.read()
            metadata = src.profile
            bounds = src.bounds
        data = np.moveaxis(data, 0, -1)
    elif any(frmt in path for frmt in MATPLOTLIB_EXTENSIONS):
        data = plt.imread(path)
        metadata = None
        bounds = None
    elif any(frmt in path for frmt in NETCDF4_EXTENSIONS):
        data = netCDF4.Dataset(path, 'r')
        metadata = None
        bounds = None
    else:
        data = None
        metadata = None
        bounds = None
        raise Exception('Error: file can not be opened or format not supported!')
        
    return data, metadata, bounds
