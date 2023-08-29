import numpy as np


def get_patches(img : np.ndarray, kernel : tuple = (16, 16), stride : tuple = (16, 16)) -> np.ndarray:
    '''
        Split an image into patches

        Parameters:
        -----------
            - img : np.ndarray 
                a WxHxB image, with width W, height H and B bands
            - kernel : tuple
                Tuple of two values used to define the size of the patch
            - stride :  tuple
                Tuple of two values representing the stride to extract patches

        Returns:
        --------
            - patches : np.ndarray
                the Nx(kernel[0])x(kernel[1])xB vector containing the N patches extracted from img
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
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
                ],
            [
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
                ]
            ]  
        ) 

        # Making channels last
        img = np.moveaxis(img, 0, -1)

        patches = get_patches(img, kernel=(2, 2), stride=(1,1))
        ```

        Output:
        -------
        ```python
        [[[[0.1 0.1 0.1]
        [0.2 0.2 0.2]]

        [[0.4 0.4 0.4]
        [0.5 0.5 0.5]]]


        [[[0.2 0.2 0.2]
        [0.3 0.3 0.3]]

        [[0.5 0.5 0.5]
        [0.6 0.6 0.6]]]


        [[[0.3 0.3 0.3]
        [0.3 0.3 0.3]]

        [[0.6 0.6 0.6]
        [0.6 0.6 0.6]]]


        [[[0.4 0.4 0.4]
        [0.5 0.5 0.5]]

        [[0.7 0.7 0.7]
        [0.8 0.8 0.8]]]


        [[[0.5 0.5 0.5]
        [0.6 0.6 0.6]]

        [[0.8 0.8 0.8]
        [0.9 0.9 0.9]]]


        [[[0.6 0.6 0.6]
        [0.6 0.6 0.6]]

        [[0.9 0.9 0.9]
        [0.9 0.9 0.9]]]


        [[[0.7 0.7 0.7]
        [0.8 0.8 0.8]]

        [[0.7 0.7 0.7]
        [0.8 0.8 0.8]]]


        [[[0.8 0.8 0.8]
        [0.9 0.9 0.9]]

        [[0.8 0.8 0.8]
        [0.9 0.9 0.9]]]


        [[[0.9 0.9 0.9]
        [0.9 0.9 0.9]]

        [[0.9 0.9 0.9]
        [0.9 0.9 0.9]]]]
        ```
    '''

    if len(img.shape) != 3:
        raise Exception("Error: len of img.shape must be 3")
    if kernel[0] < 1 or kernel[1] < 1:
        raise Exception("Error: kernel must be grather than 1")
    if stride[0] < 1 or stride[1] < 1:
        raise Exception("Error: kernel must be grather than 1")
    

    w, h, c = img.shape


    if kernel[0] > w or kernel[1] > h:
        raise Exception("Error: kernel size cannot be grather than image size")
    if stride[0] > w or stride[1] > h:
        raise Exception("Error: stride cannot be grather than image size")
    

    
    N = len(range(0, w, stride[0])) * len(range(0, h, stride[1]))
    patches = np.zeros((N, kernel[0], kernel[1], c))

    ct = 0
    for ww in range(0, w, stride[0]):
        for hh in range(0,  h, stride[1]):         
            patches[ct, ...] = img[ww:ww+kernel[0],hh:hh+kernel[1],:]
            ct += 1

    return patches


def patches_generator(img : np.ndarray, kernel : tuple = (16, 16), stride : tuple = (16, 16), batch_size : int = 1) -> np.ndarray:
    '''
        Split an image into patches

        Parameters:
        -----------
            - img : np.ndarray 
                a WxHxB image, with width W, height H and B bands
            - kernel : tuple
                Tuple of two values used to define the size of the patch
            - stride :  tuple
                Tuple of two values representing the stride to extract patches
            - batch_size : int
                integere representing how many patches yield at each iteration

        Returns:
        --------
            - patches : np.ndarray
                the (batch_size)x(kernel[0])x(kernel[1])xB vector containing the N patches extracted from img
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
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
                ],
            [
                [0.1, 0.2, 0.3],  
                [0.4, 0.5, 0.6],  
                [0.7, 0.8, 0.9]
                ]
            ]  
        ) 

        # Making channels last
        img = np.moveaxis(img, 0, -1)

        patches = patches_generator(img, kernel=(2, 2), stride=(1,1), batch_size = 1)
        ```

        Output:
        -------
        ```python
        
        ```
    '''

    if len(img.shape) != 3:
        raise Exception("Error: len of img.shape must be 3")
    if kernel[0] < 1 or kernel[1] < 1:
        raise Exception("Error: kernel must be grather than 1")
    if stride[0] < 1 or stride[1] < 1:
        raise Exception("Error: kernel must be grather than 1")
    if batch_size < 1:
        raise Exception("Error: batch_size must be grather than 1")
    

    w, h, c = img.shape


    if kernel[0] > w or kernel[1] > h:
        raise Exception("Error: kernel size cannot be grather than image size")
    if stride[0] > w or stride[1] > h:
        raise Exception("Error: stride cannot be grather than image size")
    
    
    patches = np.zeros((batch_size, kernel[0], kernel[1], c))   

    
    ct = 0 
    for ww in range(0, w-stride[0], stride[0]):
        for hh in range(0,  h-stride[1], stride[1]):

            patches[ct, :kernel[0], :kernel[1], :] = img[ww:ww+kernel[0],hh:hh+kernel[1],:]

            if ct == batch_size-1:
                ct = 0
                yield patches
            else: ct += 1