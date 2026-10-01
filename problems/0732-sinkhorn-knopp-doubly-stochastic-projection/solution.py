import numpy as np

def sinkhorn_knopp(B: list, t_max: int = 20) -> list:
    M = np.exp(B)
    for t in range(t_max-1):
        M = M/np.sum(M, axis = 1, keepdims = True)
        M = M/np.sum(M, axis = 0, keepdims = True)
    return M.tolist()
