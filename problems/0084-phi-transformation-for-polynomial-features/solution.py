import numpy as np

def phi_transform(data: list[float], degree: int) -> list[list[float]]:
	output = []
	for data_point in data:
		transform = []
		for i in range(degree + 1):
			transform.append(data_point**i)
		output.append(transform)
	return output