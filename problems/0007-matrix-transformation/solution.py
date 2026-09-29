import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A, S, T = np.array(A), np.array(S), np.array(T)
	if np.linalg.det(S) != 0 and np.linalg.det(T) != 0:
		return (np.linalg.inv(T) @ A @ S).tolist()
	else: 
		return -1
