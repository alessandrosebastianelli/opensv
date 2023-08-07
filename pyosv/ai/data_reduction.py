from sklearn.decomposition import PCA
import numpy as np

def image_PCA(img : np.ndarray, n_components : int) -> np.ndarray:
    '''

        Reduce the image dimensionality along the channells axis using PCA

        Parameters:  
        ----------  
            - img : np.ndarray
                a WxHxB image, with width W, height H and B bands (channel last)
            - n_components : int
                number of bands of the compressed image
        
        Returns:
        --------
            - reduced : np.ndarray
                the WxHxn_components compressed image, with width W, height H and n_components bands

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

        reduced = image_PCA(img, n_components = 1)
        ```
        Output:
        ------
        ```
        array([
              [[ 0.56568542],
                [ 0.42426407],
                [ 0.28284271]],
              [[0.14142136],
                [-0.        ],
                [-0.14142136]],
              [[-0.28284271],
                [-0.42426407],
                [-0.56568542]]])
       ```

    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 -  (space, space, channels)')

    pca = PCA(n_components)
    reduced = pca.fit_transform(img.reshape((img.shape[0] * img.shape[1], img.shape[2])))
    reduced = reduced.reshape((img.shape[0], img.shape[1], n_components))
    reduced = np.array(reduced)

    return reduced


def image_stack_PCA(imgs : np.ndarray, n_components : int) -> np.ndarray:
    '''
        Reduce a temporal stack of images along the temporal axis
    '''
    if len(imgs.shape) != 4:
        raise Exception('Error: lenght of imgs shape must be 4 - (space, space, channels, time)')
    
    pass