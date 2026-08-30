import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    res=0
    if(len(x)==len(y)):
        for i in range(0,len(x)):
            res+=x[i]*y[i]
    return float(res)
        
        