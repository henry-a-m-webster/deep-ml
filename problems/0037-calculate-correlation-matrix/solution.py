import numpy as np

def calculate_correlation_matrix(X, Y=None):
	n = np.shape(X)[0]
	if Y is None:
		Y = X
	X_c = X - np.mean(X, axis = 0)
	Y_c = Y - np.mean(Y, axis = 0)
	cov = 1/n * (X_c.T @ Y_c)
	sig_x = np.std(X, axis = 0)
	sig_y = np.std(Y, axis = 0)
	corr = cov/np.outer(sig_x, sig_y)
	return corr
	