import numpy as np
def orthogonal_projection(v, L):
	v, L = np.array(v), np.array(L)
	dot_prod = np.dot(v, L)
	mag_v, mag_L = np.linalg.norm(v), np.linalg.norm(L)
	vector = dot_prod/(mag_L**2) * L
	output = np.round(vector, 3).tolist()
	return output
	
