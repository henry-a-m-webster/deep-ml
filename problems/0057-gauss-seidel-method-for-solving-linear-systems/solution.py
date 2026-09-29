import numpy as np

def gauss_seidel(A, b, n, x_ini=None):
	m = len(A)
	if x_ini is None:
		x = np.zeros(m)
	else:
		x = np.array(x_ini)
	L = np.tril(A)
	U = A - L
	for _ in range(n):
		x = np.linalg.solve(L, b - U @ x)

	return x
