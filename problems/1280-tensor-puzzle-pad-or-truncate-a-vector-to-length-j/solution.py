import numpy as np

def pad_to(a: np.ndarray, j: int) -> np.ndarray:
    """Pad a with zeros (or truncate) to length j."""
    i = np.arange(j)
    n = len(a)-1
    index = np.minimum(i, n)
    return np.where(i < len(a), a[index], 0.0)
