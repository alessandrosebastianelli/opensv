import numpy as np

def dict_disp(dict):
    '''

        Print a dictionary in a more readable way

        Input:
            - dict: python dictionary to print
    '''

    print('//----------- Dictionary -----------//')

    for key, value in dict.items():
        print('\t [*] {} : {}'.format(str(key), str(value)))

def print_stats(image, perband=False):
    '''

        Print some statistics for the input image

        Inputs:
            - image: a WxHxB image, with width W, height H and B bands
            - perband (optional): if true the function will print the statistics for each band separately
    '''

    print('//----------- Image Statistics -----------//')
    print('\t [*] Shape              {}'.format(image.shape))

    if perband:
        for i in range(image.shape[-1]):
            print('\t Band #{}'.format(i))
            print('\t\t [*] Max                {0:.5f}'.format(np.max(image[:, :, i])))
            print('\t\t [*] Min                {0:.5f}'.format(np.min(image[:, :, i])))
            print('\t\t [*] Mean               {0:.5f}'.format(np.mean(image[:, :, i])))
            print('\t\t [*] Standard Deviation {0:.5f}'.format(np.std(image[:, :, i])))
            print('\t\t [*] Median             {0:.5f}'.format(np.median(image[:, :, i])))
    else:
        print('\t [*] Max                {0:.5f}'.format(np.max(image)))
        print('\t [*] Min                {0:.5f}'.format(np.min(image)))
        print('\t [*] Mean               {0:.5f}'.format(np.mean(image)))
        print('\t [*] Standard Deviation {0:.5f}'.format(np.std(image)))
        print('\t [*] Median             {0:.5f}'.format(np.median(image)))