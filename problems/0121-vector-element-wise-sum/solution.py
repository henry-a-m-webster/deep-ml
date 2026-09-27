def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1
	else: 
		output = []
		for i in range(len(a)):
			output.append(a[i] + b[i])
		return output