import numpy as np


def percentile_prescaler(data, perc=95, mmin = None):
    '''
    
        Clip data between minimum and maximum based on the percentile at perc
    
        
        Inputs:
            - data: a WxHxB image, with W width, H height and B bands            
            - perc: the percentile value
            - mmin (optional): the minimum
        Outputs:
            - data: normalized WxHxB image, with W width, H height and B bands
            
    '''
    
    if mmin == None: mmin = np.min(data)
    
    mmax = np.percentile(data, perc)
    data = np.clip(data, mmin, mmax)
    
    return data

def minmax_scaler(data, mmin=None, mmax=None, clip = [None, None]): 
    '''
    
        Apply the min max scaler to the input data. The formula is:
        
        out = (data - minimum)/(maximum - minimum + E)          (1)
        
        where E is a stabilizer term.
        
        
        Inputs:
            - data: a WxHxB image, with W width, H height and B bands
            - mmin (optional): the minimum in equation (1)
            - mmax (optional): the maximum in equation (1)
            - clip (optional): a list of two values used to constrain the image values 
        Outputs:
            - data: normalized WxHxB image, with W width, H height and B bands
            
    '''
    
    if mmin == None: mmin = np.min(data)
    if mmax == None: mmax = np.max(data)
    
    E = 0.001
    
    data = (data - mmin)/((mmax - mmin)+E)
    
    if clip != [None, None]: data = np.clip(data, clip[0], clip[1])
    
    return data

def max_scaler(data, mmax=None, clip = [None, None]): 
    '''
    
        Apply the max scaler to the input data. The formula is:
        
        out = data/maximum          (1)
        
        
        Inputs:
            - data: a WxHxB image, with W width, H height and B bands            
            - mmax (optional): the maximum in equation (1)
            - clip (optional): a list of two values used to constrain the image values 
        Outputs:
            - data: normalized WxHxB image, with W width, H height and B bands
            
    '''
    
    if mmax == None: mmax = np.max(data)
    
    data = data/mmax
    
    if clip != [None, None]: data = np.clip(data, clip[0], clip[-1])
    
    return data


def std_scaler(data, mmean=None, sstd = None, clip = [None, None]):
    '''
    
        Apply the standardizer to the input data. The formula is:
        
        out = (data - mean)/standard deviation         (1)
        
        
        Inputs:
            - data: a WxHxB image, with W width, H height and B bands            
            - mmean (optional): the mean in equation (1)
            - sstd (optional): the standard deviation in equation (1)
            - clip (optional): a list of two values used to constrain the image values 
        Outputs:
            - data: normalized WxHxB image, with W width, H height and B bands
            
    '''
    
    if mmean == None: mmean = np.mean(data)
    if sstd == None: sstd = np.std(data)
    
    data = (data - mmean)/sstd
    
    if clip != [None, None]: data = np.clip(data, clip[0], clip[-1])
    
    return data

