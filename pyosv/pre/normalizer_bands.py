import numpy as np


def percentile_prescaler(img : np.ndarray , perc : list, mmin : list = None) -> np.ndarray:
    '''
        Clip image between minimum and maximum based on the percentile
    
        Parameters:
        -----------
            - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands            
            - perc: list
                the percentile values (one for each band)
            - mmin : list
                the minimum values (one for each band) to clip the img (default : None), if None mmin is calculated from img
        
        Returns:
        --------
            - img : np.ndarray 
                normalized WxHxB image, with W width, H height and B bands

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

        img_n = percentile_prescaler(img, perc=[95,95], mmin=[0,0])
        ```

        Output:
        -------
        ```
            [[0.1  1.1 ] 
            [0.2  1.2 ]  
            [0.3  1.3 ]]  
            [[0.4  1.4 ]  
            [0.5  1.5 ]  
            [0.6  1.6 ]]  
            [[0.7  1.7 ]  
            [0.8  1.8 ]  
            [0.86 1.86]]]  
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    if mmin is not None:
        if len(mmin) != img.shape[-1]:
            raise Exception('Error: lenght of mmin must be equals to number of bands')
    
    if len(perc) != img.shape[-1]:
        raise Exception('Error: lenght of perc must be equals to number of bands')


    if mmin is None: mmin = np.min(img, axis=-1)

    for i in range(img.shape[-1]):
        mmax = np.percentile(img[:,:,i], perc[i])
        img[:,:,i] = np.clip(img[:,:,i], mmin[i], mmax)
    
    return img


def minmax_scaler(img : np.ndarray, mmin : list = None, mmax : list = None, clip : list = [None, None]) -> np.ndarray: 
    '''
        Apply the min max scaler to the input img:  
        
        out = (img - minimum)/(maximum - minimum + E)          (1)  
        
        where E stabilizes the division. 
        
        Parameters:
        -----------
             - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands
            - mmin : list 
                the minimum in equation (1) (one for each band) (default : None)
            - mmax : lsit
                the maximum in equation (1) (one for each band) (default : None)
            - clip : list 
                a list of two values used to constrain the image values (default : [None, None])
        
        Returns:
        --------
            - img : np.ndarray
                normalized WxHxB image, with W width, H height and B bands

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

        img_n = minmax_scaler(img, mmin=[0,0], mmax=[1,1], clip = [0,0.5])
        ```

        Output:
        -------
        ```
        [[[0.0999001 0.5      ]  
        [0.1998002 0.5      ]  
        [0.2997003 0.5      ]]  
        [[0.3996004 0.5      ]  
        [0.4995005 0.5      ]  
        [0.5       0.5      ]]  
        [[0.5       0.5      ]  
        [0.5       0.5      ]  
        [0.5       0.5      ]]]  
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    if mmin is not None:
        if len(mmin) != img.shape[-1]:
            raise Exception('Error: lenght of mmin must be equals to number of bands')
    
    if mmax is not None:
        if len(mmax) != img.shape[-1]:
            raise Exception('Error: lenght of mmax must be equals to number of bands')
    
    E = 0.001

    if mmin == None: mmin = np.min(img, axis=-1)
    if mmax == None: mmax = np.max(img, axis=-1)
    
    for i in range(img.shape[-1]):    
        img[:,:,i] = (img[:,:,i] - mmin[i])/((mmax[i] - mmin[i]) + E)
    
    if clip is not None: img = np.clip(img, clip[0], clip[-1])
    
    return img


def std_scaler(img : np.ndarray, mmean : list = None, sstd : list = None, clip : list = [None, None]) -> np.ndarray:
    '''
        Apply the min max scaler to the input img:  
        
        out = (img - mean)/(std)             (1)  
         
        Parameters:
        -----------
             - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands
            - mmean : list 
                the mean in equation (1) (one for each band) (default : None)
            - sstd : lsit
                the standar deviation in equation (1) (one for each band) (default : None)
            - clip : list 
                a list of two values used to constrain the image values (default : [None, None])
        
        Returns:
        --------
            - img : np.ndarray
                normalized WxHxB image, with W width, H height and B bands

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

        img_n = std_scaler(img, None, None, clip = [0,0.5])
        ```

        Output:
        -------
        ```
            [[[0.  0.4]  
            [0.  0.4]  
            [0.  0.4]]  
            [[0.  0.5]  
            [0.  0.5]  
            [0.  0.5]]  
            [[0.2 0.5]  
            [0.2 0.5]  
            [0.2 0.5]]]   
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    if mmean is not None:
        if len(mmean) != img.shape[-1]:
            raise Exception('Error: lenght of mmin must be equals to number of bands')
    
    if sstd is not None:
        if len(sstd) != img.shape[-1]:
            raise Exception('Error: lenght of mmax must be equals to number of bands')
    
    if mmean == None: mmean = np.mean(img, axis=-1)
    if sstd  == None: sstd  = np.std(img, axis=-1)
    
    for i in range(img.shape[-1]):    
        img[:,:,i] = (img[:,:,i] - mmean[i])/(sstd[i])
    
    if clip is not None: img = np.clip(img, clip[0], clip[-1])
    
    return img