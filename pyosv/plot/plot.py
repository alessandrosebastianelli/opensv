import matplotlib.pyplot as plt
import numpy as np

def plot(img, hist = False):
    '''
        Plot an image and its histogram
        
        Inputs:
            - img: a WxHxB image, with width W, height H and B bands (B can be 3 or 1)
            - hist (optional): if True display also the histogram
    '''
    
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


def bands_plot(img, hist = False):
    '''
        Plot image bands and relative histograms
        
        Inputs:
            - img: a WxHxB image, with width W, height H and B bands
            - hist (optional): if True display also the histogram
    '''    
    
    bands = img.shape[-1]
    nrows = int(np.sqrt(bands))
    

    ncols = nrows
    if hist: ncols = 2*nrows
    
    fig, axes = plt.subplots(nrows = nrows, ncols = ncols, figsize = (4*ncols, 4*nrows))
    
    if hist: ncols = nrows
    
    ct = 0
    for r in range(nrows):
        for c in range(ncols):
            if hist:
                axes[r,2*c].imshow(img[:,:,ct])
                axes[r,2*c].set_title('Bands {}'.format(ct))
                
                axes[r,2*c+1].hist(img[:,:,ct].flatten(), 200)
                axes[r,2*c+1].set_title('Histogram of Band {}'.format(ct))
            else:
                axes[r,c].imshow(img[:,:,ct])
                axes[r,c].set_title('Band {}'.format(ct))
            ct+=1

    fig.tight_layout()
    plt.show()