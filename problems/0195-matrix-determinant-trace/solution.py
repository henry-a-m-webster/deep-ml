import numpy as np

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	trace = np.trace(np.array(matrix))
	determinant = np.linalg.det(np.array(matrix))
	return (determinant, trace)