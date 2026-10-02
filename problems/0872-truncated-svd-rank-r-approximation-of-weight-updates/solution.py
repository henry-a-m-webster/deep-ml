import numpy as np

def low_rank_approximation(delta_W: np.ndarray, r: int) -> list:
	"""
	Compute the best rank-r approximation of delta_W via truncated SVD.

	Args:
		delta_W: matrix of shape (m, n)
		r: target rank (1 <= r <= min(m, n))

	Returns:
		The rank-r approximation as a nested Python list of shape (m, n).
	"""
	# Your code here
	U, S, Vh = np.linalg.svd(delta_W)
	U_r = U[:, :r]
	V_r = Vh.T[:, :r]
	S_r = np.diag(S[:r])
	output = U_r @ S_r @ V_r.T
	return output.tolist()
	