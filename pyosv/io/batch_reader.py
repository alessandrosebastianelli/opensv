from ..utils.paths import get_path_gui

from rasterio.windows import Window
import numpy as np
import rasterio


def load(path : str, patch_shape : tuple = (64,64)) -> np.ndarray:
    '''
        Load an image patch by patch

        Supported data format

        RASTERIO_EXTENSIONS   = ['.tif', '.tiff', '.geotiff']  
        MATPLOTLIB_EXTENSIONS = ['.png', '.jpg', 'jpeg']

        Returns always data in channel last format.

        If image extension is in MATPLOTLIB_EXTENSIONS, metadata and bound will be None.
        
        Parameters:
        -----------
            - path : str
                position of the image, if None the function will ask for the image path using a menu
            - patch_shape :  tuple[int,int]
                tuple of two integers representing the size of the patches to be loaded from the image

        Returns:
        --------
            - data : np.ndarray
                patch_shape[0]xpatch_shape[1]xB image patch, with patch_shape[0] width, patch_shape[1] height and B bands
        
        Usage:
        ------
        ```python
            iterator = iter(
                load(None, patch_size = (64,64))
                )

                patch = next(iterator) 
        ``` 
        or
        ```python
            img = iter(
                load("path/to/image.png")
                )
            patch = next(iterator) 

        ``` 

        Output:
        -------
        ```
        P1:

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
                    [1330., 1032.,  833., ...,    0.,    0.,    0.]]])
        
        P2:
            array([[[1015.,  741.,  673., ...,    0.,    0.,    0.],  
                    [1015.,  729.,  676., ...,    0.,    0.,    0.],  
                    [1015.,  757.,  670., ...,    0.,    0.,    0.],  
                    ...,  
                    [1039.,  764.,  692., ...,    0.,    0.,    0.],  
                    [1039.,  752.,  702., ...,    0.,    0.,    0.],  
                    [1039.,  761.,  736., ...,    0.,    0.,    0.]],  
                    ...,  
                    [[1012.,  728.,  630., ...,    0.,    0.,    0.],  
                    [1012.,  742.,  686., ...,    0.,    0.,    0.],  
                    [1012.,  754.,  724., ...,    0.,    0.,    0.],  
                    ...,  
                    [1033.,  773.,  715., ...,    0.,    0.,    0.],  
                    [1033.,  768.,  733., ...,    0.,    0.,    0.],  
                    [1033.,  763.,  745., ...,    0.,    0.,    0.]]])  

        ```
    '''

    RASTERIO_EXTENSIONS = ['.tif', '.tiff']

    if path is None:
        path = get_path_gui()

    if any(frmt in path for frmt in RASTERIO_EXTENSIONS):

        with rasterio.open(path) as src:
            c, w, h = src.read().shape

        for i in range(0, w - patch_shape[0], patch_shape[0]):
            for j in range(0, h -  patch_shape[1], patch_shape[1]):

                with rasterio.open(path) as src:
                    data = src.read(window=Window(j, i, patch_shape[1], patch_shape[0]))
                    data = np.moveaxis(data, 0, -1)
                yield data
    else:
        raise Exception('Error: file can not be opened or format not supported!')