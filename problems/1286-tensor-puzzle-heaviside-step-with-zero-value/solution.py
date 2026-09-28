import numpy as np

def heaviside(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Element-wise heaviside with zero-value b."""
    return np.where(a < 0, 0, np.where(a == 0, b, 1))
