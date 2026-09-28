import numpy as np

def diff(a: np.ndarray) -> np.ndarray:
    """out[0]=a[0]; out[i]=a[i]-a[i-1] for i>0."""
    i = np.arange(len(a))
    output = a.copy()
    output[1:] = a[1:] - a[:-1]
    return output
