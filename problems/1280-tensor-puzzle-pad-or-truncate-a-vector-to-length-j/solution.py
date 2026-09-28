import numpy as np

def pad_to(a: np.ndarray, j: int) -> np.ndarray:
    """Pad a with zeros (or truncate) to length j."""
    output = np.zeros(j)
    n = np.minimum(len(a), j)
    output[:n] = a[:n]
    return output
