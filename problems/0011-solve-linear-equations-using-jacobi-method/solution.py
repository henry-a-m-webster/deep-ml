import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(len(b))
	i = np.arange(len(b))[:, None]
	j = np.arange(len(b))[None, :]
	for it in range(n):
		x = 1/np.diag(A)*(b - np.sum((i != j)*A[i,j]*x[j], axis = 1))
	return x
