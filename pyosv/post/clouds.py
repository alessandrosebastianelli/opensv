from ..pre.normalized_difference import normalized_difference
from ..pre.normalizer import minmax_scaler


import scipy.signal as scisig
import numpy as np
import scipy

def cloud_detector(image, cloud_threshold=None):
    '''
        Sentinel-2 cloud masking based on spectral response.
        
        Inputs:
            - image: Sentinel-2 MS WxHxB image, it must contains all the 12 bands, with W width, H height and B bands
            - cloud_threshold (optional) (std value 0.2): a value used to binarize the mask
        
        Output:
            - score: a WxH matrix representing the cloud mask
    '''
    
    (w, h, b) = image.shape
    
    # Cloud until proven otherwise
    score = np.ones((w,h)).astype('float32')
    
    # Clouds are reasonably bright in the blue and aerosol/cirrus bands.
    score = np.minimum(score, minmax_scaler(image[:,:,1], mmin = 0.1, mmax = 0.5))
    score = np.minimum(score, minmax_scaler(image[:,:,0], mmin = 0.1, mmax = 0.3))
    score = np.minimum(score, minmax_scaler(image[:,:,0]+image[:,:,10], mmin = 0.4, mmax = 0.9))
    score = np.minimum(score, minmax_scaler(image[:,:,3]+image[:,:,2]+image[:,:,1], mmin = 0.2, mmax = 0.8))
    
    # Clouds are moist
    ndmi = normalized_difference(image[:,:,7], image[:,:,11])
    score = np.minimum(score, minmax_scaler(ndmi, mmin = -0.1, mmax = 0.1))

    # However, clouds are not snow.
    ndsi = normalized_difference(image[:,:,2], image[:,:,11])
    score = np.minimum(score, minmax_scaler(ndsi, mmin = 0.8, mmax = 0.6))

    boxsize = 7
    box = np.ones((boxsize, boxsize)) / (boxsize ** 2)

    score = scipy.ndimage.morphology.grey_closing(score, size=(5, 5))
    score = scisig.convolve2d(score, box, mode='same')

    score = np.clip(score, 0.00001, 1.0)

    if cloud_threshold!=None:
        score[score >= cloud_threshold] = 1
        score[score < cloud_threshold]  = 0
        
    return score

def white_detector(image, cloud_threshold=0.8):
    '''
        Sentinel-2 cloud masking based on white pixels.
        
        Inputs:
            - image: Sentinel-2 RGB WxHx3 image, it must be the RGB composite, with W width, H height and 3 bands (RGB)
            - cloud_threshold (optional) (std value 0.8): a value used to get withe pixels and build the mask
        
        Output:
            - cm: a WxH matrix representing the cloud mask
    '''   
    
    cm = ((image[:,:,0]>cloud_threshold)+(image[:,:,1]>cloud_threshold)+(image[:,:,2]>cloud_threshold)).astype(np.int8)
    
    return cm