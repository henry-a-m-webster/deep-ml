
import numpy as np
from sympy import Matrix
def matrix_image(A):
	RREF = np.array(Matrix(A).rref()[0])
	pivots = []
	for i in range(np.shape(A)[0]):
		for j in range(np.shape(A)[1]):
			if RREF[i, j] == 1:
				pivots.append(j)
				break
	return A[:, pivots]

