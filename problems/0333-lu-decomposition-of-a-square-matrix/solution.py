import numpy as np

def lu_decomposition(A: list) -> tuple:
	matrix = np.array(A)
	rows, columns = matrix.shape
	L = np.eye(rows)
	U = np.zeros(matrix.shape)
	for i in range(rows):
		for j in range(i, rows):
			U[i, j] = matrix[i, j] - np.dot(L[i, :i], U[:i, j])
		for j in range(i + 1, rows):
			L[j, i] = 1/U[i, i]*(matrix[j, i] - np.dot(L[j, :i], U[:i, i]))
	return L, U
	