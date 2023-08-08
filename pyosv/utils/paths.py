from tkinter.filedialog import askopenfilename
from tkinter import Tk


def get_path_gui() -> str:
    
    '''
        Get the path of a file using a graphical menu    
        
        Parameters:
        -----------
        Nothing

        Returns:
        --------
            - path: path of the image

        Usage:
        ------

        ```python
        path = get_path_gui()
        ```

        Output:
        -------
        ```
        /path/to/file/img.png
        ```

    '''
    
    root = Tk()
    root.withdraw()
    path = askopenfilename(
        title='Select the file or the folder!',
        initialdir='/'
        )
    root.destroy()
    
    return path