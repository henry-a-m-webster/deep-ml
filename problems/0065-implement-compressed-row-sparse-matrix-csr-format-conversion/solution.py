import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
	dense_matrix = np.array(dense_matrix)
	rows, columns = np.shape(dense_matrix)
	values = []
	column_indices = []
	row_ptr = [0,]
	cum_sum = 0
	for i in range(rows):
		for j in range(columns):
			if dense_matrix[i,j] != 0:
				values.append((dense_matrix[i,j]).item())
				column_indices.append(j)
				cum_sum += 1
			else:
				continue
		row_ptr.append(cum_sum)
	return values, column_indices, row_ptr