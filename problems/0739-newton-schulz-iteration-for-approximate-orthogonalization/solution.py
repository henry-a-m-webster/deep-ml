import numpy as np

def newton_schulz(M, num_iters: int, a: float, b: float, c: float):
    M = np.array(M)
    F = np.linalg.norm(M, ord = 'fro')
    if F == 0:
        return np.zeros(M.shape)
    else:
        M = M/F
        for t in range(num_iters):
            M = a*M + b*(M @ M.T) @ M + c*(M @ M.T) @ (M @ M.T) @ M
    return M.astype(float).tolist()
