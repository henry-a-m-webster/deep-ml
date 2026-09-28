import numpy as np

def outer(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.transpose(a[None, :] * b[:, None])
    
