import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    matrix = arr.ravel()
    if norm_type == 'l1':
        return float(np.sum(np.abs(matrix)))
    elif norm_type == 'l2':
        return float(np.sqrt(np.sum(matrix**2)))
    elif norm_type == 'linf':
        return float(np.max(np.abs(matrix)))
    elif norm_type == 'frobenius':
        return np.linalg.norm(arr, ord = 'fro')
    else:
        raise ValueError


