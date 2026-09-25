import numpy as np

def make_diagonal(x):
	dim = len(x)
	matrix = np.zeros((dim, dim))
	for i in range(len(x)):
		matrix[i,i] = x[i]
	return matrix