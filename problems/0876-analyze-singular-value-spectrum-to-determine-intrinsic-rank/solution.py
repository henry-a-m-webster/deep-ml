import numpy as np

def suggest_rank(delta_W: np.ndarray, energy_threshold: float) -> int:
	"""
	Return the smallest rank k such that the top-k singular values of delta_W
	capture at least `energy_threshold` of the total squared-singular-value energy.
	"""
	# Your code here
	if np.allclose(delta_W, np.zeros(delta_W.shape)):
		return 0
	else:
		S = np.linalg.svd(delta_W, compute_uv = False)
		total_energy = np.sum(S**2)
		cumulative_energies = np.cumsum(S**2)/total_energy
		for j in range(len(cumulative_energies)):
			if cumulative_energies[j] >= energy_threshold:
				output = j
				break
			else:
				continue
		return j + 1