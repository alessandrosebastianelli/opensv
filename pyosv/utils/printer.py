import numpy as np

def dict_disp(dictionary : dict) -> None:
    '''
        Print a dictionary in a more readable way

        Parameter:
        ----------
            - dictionary : dict
                python dictionary to print
        
        Returns:
        --------
        Nothing, it will print the dictionary

        Usage:
        ------

        ```python
        dictionary = {'Name' : 'John', 'Surname' : 'Wick'}
        disp_dict(dictionary)
        ```

        Output:
        -------

        ```
        -----------Dictionary------------  
            [*] Name : Johnny
            [*] Surname : Wick
        ```

    '''

    l_k = len([k for k in dictionary.keys() if len(str(k))==max([len(str(n)) for n in dictionary.keys()])][0])
    l_v = len([k for k in dictionary.values() if len(str(k))==max([len(str(n)) for n in dictionary.values()])][0])

    n =  20 + l_k + l_v
    print('{:-^{len}}'.format('Dictionary', len=n))

    for key, value in dictionary.items():
        print('\t [*] {} : {}'.format(str(key), str(value)))


def print_stats(img : np.ndarray, bandwise : bool = False) -> None:
    '''
        Print some statistics for the input image

        Parameters:
        -----------
            - image: a WxHxB image, with width W, height H and B bands
            - bandwise : bool 
                if true the function will print the statistics for each band separately (default : False)
        
        Returns:
        --------
        Nothing, it will print image statistics

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

        print_stats(img, bandwise = True)

        ```

        Output:
        -------

        ```
        ```
    '''

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')

    print('{:-^{len}}'.format('Image Statistics', len=50))
    print('{:<20s}{}'.format('[*] Shape', img.shape))

    if bandwise:
        for i in range(img.shape[-1]):
            print('{:<20s}'.format('Band '+str(i)))
            print('\t{:<20s}{:<30s}'.format('[*] Max',  str(np.max(img[:, :, i]))))
            print('\t{:<20s}{:<30s}'.format('[*] Min',  str(np.min(img[:, :, i]))))
            print('\t{:<20s}{:<30s}'.format('[*] Mean', str(np.mean(img[:, :, i]))))
            print('\t{:<20s}{:<30s}'.format('[*] Std',  str(np.std(img[:, :, i]))))
            print('\t{:<20s}{:<30s}'.format('[*] Med',  str(np.median(img[:, :, i]))))
    else:
        print('{:<20s}{:<30s}'.format('[*] Max',  str(np.max(img))))
        print('{:<20s}{:<30s}'.format('[*] Min',  str(np.min(img))))
        print('{:<20s}{:<30s}'.format('[*] Mean', str(np.mean(img))))
        print('{:<20s}{:<30s}'.format('[*] Std',  str(np.std(img))))
        print('{:<20s}{:<30s}'.format('[*] Med',  str(np.median(img))))