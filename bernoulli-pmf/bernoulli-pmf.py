import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    pmf=[]
    for i in x:
        if(i==1):
            pmf.append(p)
        else:
            pmf.append(1-p)
    mean=p
    variance=p*(1-p)
    return {"pmf":np.array(pmf),"mean":float(mean),"variance":float(variance)}