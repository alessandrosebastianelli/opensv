from tkinter.filedialog import askopenfilename
from tkinter import Tk


def get_path_gui():
    
    '''
        Get the path of a file using a graphical menu    
        
        Output:
            - path: path of the image
    '''
    
    root = Tk()
    root.withdraw()
    path = askopenfilename(
        title='Select the image to read!',
        initialdir='/'
        )
    root.destroy()
    
    return path