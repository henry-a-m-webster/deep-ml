import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	rows, columns = len(a), len(a[0])
	if rows*columns == new_shape[0]*new_shape[1]:
		reshaped_matrix = []
		flattened = []
		for i in range(len(a)):
			for j in range(len(a[0])):
				flattened.append(a[i][j])
		for l in range(new_shape[0]):
			start = l*new_shape[1]
			end = start + new_shape[1]
			reshaped_matrix.append(flattened[start:end])
		return reshaped_matrix
	else: 
		return []