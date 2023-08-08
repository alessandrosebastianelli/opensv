import numpy as np

def mapFromTo(x : np.ndarray , a : int, b : int, c : int, d : int) -> np.ndarray:
    '''
        Map x from range a,b to range c,d
        
        Parameters:
        -----------
            - x : np.ndarray
                input to be mapped
            - a : int 
                min range from, if None it will inputed using x
            - b : int
                max range from, if None it will inputed using x
            - c : int
                min range to
            - d : int
                max range to
        
        Returns:
        --------
            - y : np.ndarray
                mapped values
        
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

        img_m = mapFromTo(img, None, None, 0, 255)
        ```

        Output:
        -------

        ```
        [[[  0.          14.16666667  28.33333333]  
        [ 42.5         56.66666667  70.83333333]  
        [ 85.          99.16666667 113.33333333]]  
        [[141.66666667 155.83333333 170.        ]  
        [184.16666667 198.33333333 212.5       ]  
        [226.66666667 240.83333333 255.        ]]]  
        ```
    '''

    if a is None: a = np.min(x)
    if b is None: b = np.max(x)

    # Avoid zero division
    if b-a == 0: b = 0.0001 
    if d-c == 0: d = 0.0001
    
    y = (x-a)/(b-a)*(d-c)+c
    
    return y
