import numpy as np

def eye(n: int) -> np.ndarray:
    i = np.arange(n)
    bool_mask = i[None, :] == i[:, None]
    return bool_mask.astype(float)
    
