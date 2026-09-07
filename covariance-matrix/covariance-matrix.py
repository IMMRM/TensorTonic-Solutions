import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """
    # Write code here
    X_c=X-np.mean(X,axis=0)
    center=X_c.T@X_c
    return center/(X_c.shape[0]-1)