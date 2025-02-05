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
    
    
    w, h, c = img.shape
    patches = []
    for ww in range(0, w - kernel[0] + 1, stride[0]):
        for hh in range(0,  h - kernel[1] + 1, stride[1]):         
            patches.append(img[ww:ww+kernel[0],hh:hh+kernel[1],...])

    return np.array(patches)



def reverse_get_patches(patches : np.ndarray, img_shape:tuple, kernel : tuple = (16, 16), stride : tuple = (16, 16)) -> np.ndarray:
    '''
        Reconstruct an image from its patches

        Parameters:
        -----------
            - patches : np.ndarray 
                a NxWxHxB image, with width W, height H and B bands
            - img_shape: tuple
                a tuple defining the shape of the reconstructed image (W,H,B) with width W, height H and B bands
            - kernel : tuple
                Tuple of two values used to define the size of the patch
            - stride :  tuple
                Tuple of two values representing the stride to extract patches

        Returns:
        --------
            - img : np.ndarray
                the WxHxB reconstructed image
        Usage:
        ------
        ```python
        import numpy as np  

        patches = np.array(
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
        )



        patches = reverse_get_patches(patches, img_shape=(3,3,3), kernel=(2, 2), stride=(1,1))
        ```

        Output:
        -------
        ```python
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
        ]]  
        ```
    '''

    if len(patches.shape) != 4:
        raise Exception("Error: len of img.shape must be 4")
    if kernel[0] < 1 or kernel[1] < 1:
        raise Exception("Error: kernel must be grather than 1")
    if stride[0] < 1 or stride[1] < 1:
        raise Exception("Error: kernel must be grather than 1")

    img_height, img_width, channels = img_shape
    patch_height, patch_width = kernel
    stride_y, stride_x = stride
    
    reconstructed_image = np.zeros((img_height, img_width, channels))
    count_map = np.zeros((img_height, img_width, channels))
    
    patch_index = 0
    for y in range(0, img_height - patch_height + 1, stride_y):
        for x in range(0, img_width - patch_width + 1, stride_x):
            reconstructed_image[y:y + patch_height, x:x + patch_width,...] += patches[patch_index, ...]
            count_map[y:y + patch_height, x:x + patch_width] += 1
            patch_index += 1
    
    reconstructed_image /= np.maximum(count_map, 1)

    return reconstructed_image