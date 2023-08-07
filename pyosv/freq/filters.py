import numpy as np

def gaussian_filter(fft : np.ndarray, mx : int =0, my : int = 0, sx : int = 1, sy : int = 1, invert : bool = False) -> np.ndarray:
    '''
        Apply a 2D gaussian filter to the input 2D spectrum
        
        Prameters:
        ---------
            - fft : np.ndarray 
                2D spectrum to be filtered
            - mx : int 
                mean of gaussian x function (default : 0)
            - my : int
                mean of gaussian y function (default : 0)
            - sx : int
                standard deviation of gaussian x function (default : 1)
            = sy : int
                standard deviation of gaussian y function (default : 1)
            - invert : bool
                invert the distribution (default : False)
        
        Returns:
        --------
            - filt : np.ndarray
                filtered spectrum
        
        Usage:
        ------
        ```python
        import numpy as np

        fft = np.array(
            [
            [0,   0, 1,   0,0],
            [0, 0.5, 1, 0.5,0],
            [1,   1, 1,   1,1],
            [0, 0.5, 1, 0.5,0],
            [0,   0, 1,   0,0],
            ]

        )

        filt = gaussian_filter(fft, mx=0, my=0, sx=1, sy=1, invert=False)
        ```

        Output:
        -------
        ```
        array([  
            [0.        , 0.        , 0.09653235, 0.        , 0.        ],  
            [0.        , 0.061975  , 0.14045374, 0.061975  , 0.        ],  
            [0.09653235, 0.14045374, 0.15915494, 0.14045374, 0.09653235],  
            [0.        , 0.061975  , 0.14045374, 0.061975  , 0.        ],  
            [0.        , 0.        , 0.09653235, 0.        , 0.        ]])  
        ```
    '''

    if len(fft.shape) < 2:
        raise Exception("Error: the shape of fft must be greater than 2")
    
    x = np.linspace(-1, 1, fft.shape[0])
    y = np.linspace(-1, 1, fft.shape[1])
    
    x, y = np.meshgrid(x,y)

    fxy = 1. / (2. * np.pi * sx * sy) * np.exp(-((x - mx)**2. / (2. * sx**2.) + (y - my)**2. / (2. * sy**2.)))

    if invert: fxy = 1-fxy
    
    filt = fft*fxy
    
    return filt


def lhp_filter(fft, radius=0.5, invert=False):
    '''
        Apply a low pass or high pass filter to the input 2D spectrum
        
        Parameters:
        -----------
            - fft : np.ndarray
                2D spectrum to be filtered
            - radius : int
                size of the filter, ammited range [0-1], will mask to zero fft values lower than radius (default : 0.5)
            - invert: bool
                invert the distribution (default : False)

        Returns:
        --------
            - fft : np.ndarray
                filtered spectrum

        
        Usage:
        ------
        ```python
        import numpy as np

        fft = np.array(
            [
            [0,   0, 1,   0,0],
            [0, 0.5, 1, 0.5,0],
            [1,   1, 1,   1,1],
            [0, 0.5, 1, 0.5,0],
            [0,   0, 1,   0,0],
            ]

        )

        filt = lhp_filter(fft, radius=0.8, invert=False)
        ```

        Output:
        -------
        ```
        array([  
            [0., 0., 1., 0., 0.],  
            [0., 0., 0., 0., 0.],  
            [1., 0., 0., 0., 1.],  
            [0., 0., 0., 0., 0.],  
            [0., 0., 1., 0., 0.]])  
        ```
    '''
    
    if len(fft.shape) < 2:
        raise Exception("Error: the shape of fft must be greater than 2")
    
    x = np.linspace(-1, 1, fft.shape[0])
    y = np.linspace(-1, 1, fft.shape[1])
    x, y = np.meshgrid(x, y)

    fxy = np.sqrt(x**2 + y**2)

    if invert: fxy = 1-fxy

    fft[fxy<radius] = 0
    
    return fft