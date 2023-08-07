def mapFromTo(x, a, b, c, d):
    '''
        Map x from range a,b to range c,d
        
        Inputs:
            - x: input to be mapped
            - a: min range from
            - b: max range from
            - c: min range to
            - d: max range to
        Ouptu:
            - y: mapped values
    '''
    
    y = (x-a)/(b-a)*(d-c)+c
    
    return y