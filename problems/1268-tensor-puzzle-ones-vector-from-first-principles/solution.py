import numpy as np

def ones(n: int) -> np.ndarray:
    output = (np.arange(n) * 0) + 1
    return output.astype(np.float64)
