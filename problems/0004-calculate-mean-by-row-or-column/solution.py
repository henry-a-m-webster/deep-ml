def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	rows, columns = len(matrix), len(matrix[0])
	if mode == 'row':
		for row in matrix:
			row_sum = sum(row)
			means.append(round(row_sum/columns, 2))
	elif mode == 'column':
		for i in range(columns):
			column_sum = 0
			for row in matrix:
				column_sum += row[i]
			means.append(round(column_sum/rows, 2))
	return means