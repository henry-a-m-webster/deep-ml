import numpy as np

def roll(a: np.ndarray) -> np.ndarray:
    """Circular left shift by one."""
    # Your code here
    n = len(a)
    output = a.copy()
    i = np.arange(n)
    output[i] = a[(i + 1)%n]
    return output
    
