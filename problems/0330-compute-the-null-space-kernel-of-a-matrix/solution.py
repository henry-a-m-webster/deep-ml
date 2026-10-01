import numpy as np

def compute_null_space(A: np.ndarray, tol: float = 1e-10) -> np.ndarray:
    nullity = np.shape(A)[1] - np.linalg.matrix_rank(A)
    if nullity != 0:
        U, S, Vh = np.linalg.svd(A)
        V = Vh.T
        r = np.linalg.matrix_rank(A)
        output = V[:, r:]
    else:
        output = np.empty((np.shape(A)[1],0))
    return output
