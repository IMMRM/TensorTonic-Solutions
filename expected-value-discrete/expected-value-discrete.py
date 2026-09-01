import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    if(len(x)==len(p)):
        sum_val=0
        for xi,pi in zip(x,p):
            sum_val+=(xi*pi)
    return float(sum_val)