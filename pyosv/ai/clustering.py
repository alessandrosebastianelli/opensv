from sklearn.cluster import KMeans
import numpy as np

def pixel_clustering(img : np.ndarray, n_clusters : int = 3) -> np.ndarray:
    '''
        Image pixel clustering using Support Vector machine
        
        Parameters:
        -----------
            - img : np.ndarray  
                a WxHxB image, with width W, height H and B bands
            - n_clusters : int  
                number of cluster to be identified
        
        Returns:
        --------
            - clusters : np.ndarray  
                clustered pixels

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

        clusters = pixel_clustering(img, nclusters = 2)
        ```
        Output:
        ------

    '''
    
    image_2D = img.reshape(img.shape[0]*img.shape[1], img.shape[2])
    kmeans = KMeans(n_clusters = n_clusters, random_state = 0).fit(image_2D)
    clusters = np.array(kmeans.labels_).reshape(img.shape[0], img.shape[1])
    
    return clusters

def conv_clustering(): pass