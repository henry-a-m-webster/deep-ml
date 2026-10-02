import numpy as np

def projection_amplification(W: list[list[float]], delta_W: list[list[float]], r: int) -> float:
	"""
	Compute the amplification factor of delta_W with respect to W
	using the top-r singular subspaces of delta_W.

	Returns: ||delta_W||_F / ||U_r^T W V_r||_F
	"""
	W, delta_W = np.array(W), np.array(delta_W)
	U, S, Vh = np.linalg.svd(delta_W)
	left = U[:,:r]
	right = Vh.T[:,:r]
	proj = left @ left.T @ W @ right @ right.T
	return np.linalg.norm(delta_W, ord = 'fro')/np.linalg.norm(proj, ord = 'fro')



	pass