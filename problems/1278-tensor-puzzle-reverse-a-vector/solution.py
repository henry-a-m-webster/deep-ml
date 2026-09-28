import numpy as np

def flip(a: np.ndarray) -> np.ndarray:
    """Reverse 1-D array a without slicing a[::-1]."""
    # Your code here
    n = len(a)
    i = np.arange(n)
    output = a.copy()
    output[i] = output[n - 1 - i]
    return output
