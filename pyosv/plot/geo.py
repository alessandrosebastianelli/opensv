import numpy as np

def geo_plot(img : np.ndarray, metadata : dict, bounds : list) -> None:
    '''
        Overlay a satellite image on a map

        Parameters:
        -----------
            - img : np.ndarray
                the WxHxC image to be plotted, with W width, H height and B bands (channel last)
            - metadata : dict
                metadata for the image to be saved
            - bounds : list
                list of geo bounds for the image
        
        Returns:
        --------
        Nothing an image is displayed

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
            
        meta = {'driver': 'GTiff',  
                'dtype': 'float64',  
                'nodata': None,  
                'width': 3,  
                'height': 3,  
                'count': 2,  
                'crs': CRS.from_epsg(32632),  
                'transform': Affine(10.0, 0.0, 638640.0, 0.0, -10.0, 5084590.0),  
                'blockxsize': 3,  
                'blockysize': 3,  
                'tiled': True,  
                'compress': 'lzw',  'interleave': 'pixel'  
                }  

        bounds = BoundingBox(left=638640.0, bottom=5074190.0, right=649070.0, top=5084590.0))  

        geo_plot(img, meta, bounds)
        ```

        Output:
        ------
        Nothing, the image is displayed
    '''
    pass