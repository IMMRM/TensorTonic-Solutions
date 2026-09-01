import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    mean=np.mean(x)
    total_sum=0
    for i in x:
        total_sum+=(i-mean)**2
    s2=total_sum/(len(x)-1)
    dev=np.sqrt(s2)
    return {"variance":float(s2),"standard_deviation":float(dev)}
        