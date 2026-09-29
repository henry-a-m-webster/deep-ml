import numpy as np

def rref(matrix):
	matrix = matrix.astype(float)
	row_len, col_len = matrix.shape
	locked = []

	for column in range(col_len):
		#select pivot row
		pivot_row = -1
		for row in range(row_len):
			if row in locked:
				continue
			if matrix[row, column] != 0:
				pivot_row = row
				break
		#if pivot hasnt changed due to selection, ignore this column as it is already in RREF form
		if pivot_row == -1:
			continue
		
		#we need the pivot row to be the row under the last locked row

		correct_row = (locked[-1] + 1) if len(locked) > 0 else 0
		
		if pivot_row != correct_row:
			matrix[[correct_row, pivot_row]] = matrix[[pivot_row, correct_row]]
			pivot_row = correct_row
		pivot_value = matrix[pivot_row, column]
		matrix[pivot_row] = matrix[pivot_row]/pivot_value

		#eliminate the following rows except pivot row
		for row in range(row_len):
			if row == pivot_row:
				continue
			lead_coeff = matrix[row, column]
			matrix[row] = matrix[row] - lead_coeff*matrix[pivot_row]
		
		locked.append(pivot_row)
	return matrix

