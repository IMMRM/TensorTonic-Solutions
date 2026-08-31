from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    mean=np.mean(x)
    median=np.median(x)
    count=Counter(x)
    max_count=max(count.values())

    #Smallest values
    min_val= min(value for value,freq in count.items() if freq==max_count)
    return {"mean":float(mean),"median":float(median),"mode":float(min_val)}