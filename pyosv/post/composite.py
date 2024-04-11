import numpy as np
from ..pre.normalizer import minmax_scaler

def S1_RGB(s1_image : np.ndarray, clip_values_rgb : list = [0.3, 0.05, 25]) -> np.ndarray:
    '''
        Generate an RGB composite of VV and VH bands of Sentinel-1.
        This function works only with double raw GRD S1 data.
        Ref. https://gis.stackexchange.com/questions/400726/creating-composite-rgb-images-from-sentinel-1-channels
        
        
        Parameters:
        -----------
            - s1_image : np.ndarray 
                WxHxB (VV and VH) Sentinel-1 data
            - clip_values_rgb : list
                list of clip values (max) to adjust color balance in the RGB composite (dafault [0.3, 0.05, 25])
        
        Returns:
        --------
            - nd : np.ndarray
                WxHxB S1 RGB composite
        
        Usage:
        ------
        ```python
        s1_image, _, _ = pyosv.io.read.load('s1.tif')
        rgb_s1 = S1_RGB(s1_image, clip_values_rgb = [0.3, 0.05, 25])
        ```

    '''

    if len(s1_image.shape) != 3:
        raise Exception('Error: lenght of s1_image shape must be 3 - (space, space, channels)')
    
    if s1_image.shape[-1] != 2:
        raise Exception('Error: s1_image channels must be 2 - (VV, VH)')
    
    if len(clip_values_rgb) != 3:
        raise Exception('Error: lenght of clip_values_rgb must be 3 - (clip for R, clip for G, clip for B)')

    vv_band = s1_image[:,:,0]
    vh_band = s1_image[:,:,1]
    # Clip values derived from [1]
    vv_band = np.clip(vv_band, 0.0, clip_values_rgb[0])
    vh_band = np.clip(vh_band, 0.0, clip_values_rgb[1])
    
    vv_band_norm = minmax_scaler(vv_band)
    vh_band_norm = minmax_scaler(vh_band)

    # Calculate ratio of VV/VH
    ratio_band = np.divide(vv_band_norm, vh_band_norm, where=vh_band_norm != 0)
    
    # Clip values derived from [1]
    ratio_band = np.clip(ratio_band, 0, clip_values_rgb[2])
    
    # Create RGB composite
    rgb = np.dstack((vv_band_norm, vh_band_norm, ratio_band))
    
    
    return rgb