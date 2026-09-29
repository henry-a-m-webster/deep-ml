import numpy as np
def translate_object(points, tx, ty):
	matrix_p = np.array(points).T
	matrix_hom = np.concatenate((matrix_p, np.ones((1, len(points)))), axis = 0)
	translation = np.array([[1, 0, tx], [0, 1, ty], [0, 0, 1]])
	output = translation @ matrix_hom
	return output[:2].T.tolist()
