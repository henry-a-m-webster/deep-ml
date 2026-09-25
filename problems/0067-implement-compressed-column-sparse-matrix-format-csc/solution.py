import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	dense_matrix = np.array(dense_matrix)
	rows, columns = np.shape(dense_matrix)
	values = []
	row_indices = []
	column_pointer = [0,]
	cum_sum = 0
	for j in range(columns):
		for i in range(rows):
			if dense_matrix[i, j].item() != 0:
				values.append(dense_matrix[i, j].item())
				row_indices.append(i)
				cum_sum += 1
			else:
				continue
		column_pointer.append(cum_sum)
	return values, row_indices, column_pointer
