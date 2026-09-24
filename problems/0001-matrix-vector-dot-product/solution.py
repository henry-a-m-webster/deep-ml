def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	output = []
	if len(b) != len(a[0]):
		return -1
	for row in a:
		row_sum = 0 
		for i in range(len(row)):
				row_sum += row[i] * b[i]
		output.append(row_sum)
	return output