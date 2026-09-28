import numpy as np

def diag(A: np.ndarray) -> np.ndarray:
    i = np.arange(min(np.shape(A)))
    return A[i, i]
    
