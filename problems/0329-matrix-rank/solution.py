import numpy as np
from sympy import Matrix

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    RREF, pivot_indices = Matrix(A.T).rref()
    return len(pivot_indices)