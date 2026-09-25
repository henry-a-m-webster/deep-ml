import numpy as np
def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    mat_arr = np.array(matrix)
    if np.linalg.det(mat_arr) == 0:
        return None
    inverse = np.linalg.inv(mat_arr)
    return inverse.tolist()