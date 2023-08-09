import numpy as np


def percentile_prescaler(img : np.ndarray , perc : int, mmin : float = None) -> np.ndarray:
    '''
        Clip image between minimum and maximum based on the percentile
    
        Parameters:
        -----------
            - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands            
            - perc: int
                the percentile value 
            - mmin : float
                the minimum value to clip the img (default : None), if None mmin is calculated from img
        
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

        img_n = percentile_prescaler(img, perc=95, mmin=0)
        ```

        Output:
        -------
        ```
            [[[0.1   1.1  ]  
            [0.2   1.2  ]  
            [0.3   1.3  ]]  
            [[0.4   1.4  ]  
            [0.5   1.5  ]  
            [0.6   1.6  ]]  
            [[0.7   1.7  ]  
            [0.8   1.8  ]  
            [0.9   1.815]]]  
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    if mmin is None: mmin = np.min(img)
    mmax = np.percentile(img, perc)
    img = np.clip(img, mmin, mmax)
    
    return img


def minmax_scaler(img : np.ndarray, mmin : float = None, mmax : float = None, clip : list = [None, None]) -> np.ndarray: 
    '''
        Apply the min max scaler to the input img:  
        
        out = (img - minimum)/(maximum - minimum + E)          (1)  
        
        where E stabilizes the division. 
        
        Parameters:
        -----------
             - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands
            - mmin : list 
                the minimum in equation (1) (default : None)
            - mmax : lsit
                the maximum in equation (1) (default : None)
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

        img_n = minmax_scaler(img, mmin=0, mmax=1, clip = [0,0.5])
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
    
    E = 0.001
    if mmin == None: mmin = np.min(img)
    if mmax == None: mmax = np.max(img)
    img = (img - mmin)/((mmax - mmin) + E)
    if clip is not None: img = np.clip(img, clip[0], clip[-1])
    
    return img


def std_scaler(img : np.ndarray, mmean : float = None, sstd : float = None, clip : list = [None, None]) -> np.ndarray:
    '''
        Apply the min max scaler to the input img:  
        
        out = (img - mean)/(std)             (1)  
         
        Parameters:
        -----------
             - img : np.ndarray 
                a WxHxB image, with W width, H height and B bands
            - mmean : list 
                the mean in equation (1) (default : None)
            - sstd : lsit
                the standar deviation in equation (1) (default : None)
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
            [[[0.         0.17770466]  
            [0.         0.35540933]  
            [0.         0.5       ]]  
            [[0.         0.5       ]  
            [0.         0.5       ]  
            [0.         0.5       ]]  
            [[0.         0.5       ]  
            [0.         0.5       ]  
            [0.         0.5       ]]]   
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    if mmean == None: mmean = np.mean(img)
    if sstd  == None: sstd  = np.std(img)
    img = (img - mmean)/(sstd)
    
    if clip is not None: img = np.clip(img, clip[0], clip[-1])
    
    return img
