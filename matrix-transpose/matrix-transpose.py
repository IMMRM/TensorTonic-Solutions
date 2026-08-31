import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    # Write code here
    transposed=[]
    for i in range(len(A[0])):
        res=[]
        for j in range(len(A)):
            res.append(A[j][i])
        transposed.append(res)
    return np.array(transposed)
    
