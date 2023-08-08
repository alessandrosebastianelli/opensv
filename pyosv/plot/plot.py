import matplotlib.pyplot as plt
import numpy as np

def plot(img : np.ndarray, hist : bool = False) -> None:
    '''
        Plot a satellite image and its histogram.

        Only gray-scale or RGB-like are accepted.

        Parameters:
        ----------
            - img : np.ndarray
                a WxHxB image, with width W, height H and B bands (B can be 3 or 1)
            - hist : bool
                if True display also the histogram (dafault : False)
        
        Returns:
        --------
        Nothing, it will display the image

        Usage:
        ------

        ```python
        import numpy as np

        img         = np.array(  
            [[
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
             ]
            ]  
        ) 

        # Adding fake axis
        img = img[:,:,None]

        plot(img, hist=True)

        ```

        Output:
        -------
        Nothing, it will display the image
    '''
    

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')

    if ((img.shape[-1] != 1) and (img.shape[-1] != 3)):
        raise Exception("Error: numer of channels admitted are 1 or 3")


    ncols = 1
    if hist: ncols = 2
    
    fig, axes = plt.subplots(nrows = 1, ncols = ncols, figsize = (4*ncols, 4))

    if hist:
        axes[0].imshow(img)
        axes[0].set_title('Image')
        for b in range(img.shape[-1]):
            axes[1].hist(img[:,:,b].flatten(), 200, label='Band {}'.format(b))
        axes[1].legend()
        axes[1].set_title('Histogram')
    else:
        axes.imshow(img)
        axes.set_title('Image')
        
    fig.tight_layout()
    plt.show()


def bands_plot(img : np.ndarray, hist : bool = False) -> None:
    '''
        Plot a satellite image bands and relative histograms.

        Parameters:
        ----------
            - img : np.ndarray
                a WxHxB image, with width W, height H and B bands
            - hist : bool
                if True display also the histograms (dafault : False)
        
        Returns:
        --------
        Nothing, it will display the image

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

        # Adding fake axis
        img = np.moveaxis(img, 0, -1)

        bands_plot(img, hist=True)

        ```

        Output:
        -------
        Nothing, it will display the image
    '''
    
    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')
    
    ncols = img.shape[-1]
    nrows = 1
    if hist: nrows = 2
    
    fig, axes = plt.subplots(nrows = nrows, ncols = ncols, figsize = (4*ncols, 4*nrows))

    for c in range(ncols):
        
        if hist:
            axes[0,c].imshow(img[:,:,c])
            axes[0,c].set_title('Bands {}'.format(c))
                
            axes[1,c].hist(img[:,:,c].flatten(), 200)
            axes[1,c].set_title('Histogram of Band {}'.format(c))
        else:
            axes[c].imshow(img[:,:,c])
            axes[c].set_title('Band {}'.format(c))

    fig.tight_layout()
    plt.show()