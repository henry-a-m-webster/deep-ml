import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    matrix = np.array(vectors)
    if np.linalg.matrix_rank(matrix) == matrix.shape[0]:
        return True
    else:
        return False
    