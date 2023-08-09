from ..utils.mapper import mapFromTo


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, mainloop, Scale, HORIZONTAL
import matplotlib.pyplot as plt
import numpy as np


def hist_normalizer(img : np.ndarray) -> None:
    '''
        Open a gui that helps to stretch the histogram of an image
     
        Parameters:
        -----------
            - img : np.ndarray 
                a WxHxB image, with width W, height H and B bands
        
        Returns:
        --------
        Nothing, it will display and image

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

        hist_normalizer(img)
        ```

        Output:
        -------
        Nothing, it will display an image
    '''
    

    if len(img.shape) != 3:
        raise Exception('Error: lenght of image shape must be 3 - (space, space, channels)')

    # Update plot
    def plot(img):
        # Clear axis
        axes[0].cla()
        axes[1].cla()
        
        # Plot image and histogram
        axes[0].set_title('Image')
        img = mapFromTo(img, wmin.get(), wmax.get(), 0, 1)
        axes[0].imshow(img)
    
        axes[1].set_title('Histogram')
        axes[1].set_xlabel('Mapped Pixel Values')
        axes[1].set_ylabel('Frequency')
    
        for k in range(img.shape[-1]):
            axes[1].hist(img[:,:,k].flatten(), 200, label = 'Band-{}'.format(k))   
            
        axes[1].legend()
        chart_type.draw()
    
    # Scale values using the sliders
    def scalevalue(value, other = img):
        image = np.clip(img, wmin.get(), wmax.get())    
        plot(image)
    
    figure, axes = plt.subplots(nrows = 1, ncols = 2, figsize=(10,5), dpi=100)
    
    # GUI
    root = Tk()
    root.title('Histrogram Scaler')
    #root.geometry('1000x620')
    #root.resizable(False, False)
    
    chart_type = FigureCanvasTkAgg(figure, root)
    chart_type.get_tk_widget().pack()
    
    wmin = Scale(root, from_=np.min(img), to=np.max(img), length = 400, label='Minimum', orient=HORIZONTAL, command = scalevalue)
    wmin.set(np.min(img))
    wmin.pack()
    wmax = Scale(root, from_=np.min(img), to=np.max(img), length = 400, label='Maximum', orient=HORIZONTAL, command = scalevalue)
    wmax.set(np.max(img))
    wmax.pack()
    
    mainloop()