from sklearn.decomposition import PCA
import numpy as np

def image_PCA(image : np.ndarray, n_components : int) -> np.ndarray:
    '''

        Reduce the image dimensionality along the channells axis using PCA

        Parameters:  
        ----------  
            - image : np.ndarray
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
        ``` python
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

    pca = PCA(n_components)
    reduced = pca.fit_transform(image.reshape((image.shape[0] * image.shape[1], image.shape[2])))
    reduced = reduced.reshape((image.shape[0], image.shape[1], n_components))
    reduced = np.array(reduced)

    return reduced


def image_stack_PCA(images, n_components):
    '''

        !!!To be implemented!!!

        Reduce a temporal stack of images along the temporal axis

        Inputs:
            - images: a TxWxHxB stack of images, with T temporal length, width W, height H and B bands
            - n_components: number of bands of the compressed image
        Output:
            - reduced: the n_componentsxWxHxB compressed image, n_components temporal length, with width W, height H and B bands

    '''

    pass