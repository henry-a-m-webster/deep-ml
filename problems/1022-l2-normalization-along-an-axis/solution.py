import numpy as np

def l2_normalize(x: np.ndarray, axis: int = -1, eps: float = 1e-12) -> list:
    axis_sum = np.sum(x**2, axis = axis, keepdims = True)
    output = x/np.sqrt((axis_sum + eps))
    return output
