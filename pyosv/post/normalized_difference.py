import numpy as np

def normalized_difference(channel_1 : np.ndarray, channel_2 : np.ndarray) -> np.ndarray:
    '''
        Normalized Difference
        
        nd = (channelA - channleB)/(channelA + channle_B + E)          (1)
        
        where E stabilizes the division.
        
        Parameters:
        -----------
            - channel_1 : np.ndarray 
                channelA in equation (1)
            - channel_2 : np.ndarray
                channelB in equation (1)
        
        Returns:
        --------
            - nd : np.ndarray
                normalized difference between channelA and Channelb in equation (1)            
        
        Usage:
        ------
        ```python
        import numpy as np

        ch1 = np.array(
                    [
                        [0.1, 0.2, 0.3],
                        [0.4, 0.5, 0.6],
                        [0.7, 0.8, 0.9]
                    ]
            )

        ch2 = np.array(
                    [
                        [2.1, 2.2, 2.3],
                        [2.4, 2.5, 2.6],
                        [2.7, 2.8, 2.9]
                    ]
            )

        nd = normalized_difference(ch1, ch2)
        ```

        Output:
        -------
        ```
            [[-0.90909091 -0.83333333 -0.76923077]  
            [-0.71428571 -0.66666667 -0.625     ]  
            [-0.58823529 -0.55555556 -0.52631579]]  
        ```

    '''
    
    num = channel_1 - channel_2
    den = channel_1 + channel_2
    
    # Avoiding 0 divisions
    den[den==0] = 0.001 #E
    
    nd = num/den
    
    return nd