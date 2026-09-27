import numpy as np

def row_normalize(counts: list[list[float]]) -> list[list[float]]:
    row_sum = np.sum(np.array(counts), axis = 1, keepdims = True)
    return (np.nan_to_num(np.array(counts)/row_sum)).tolist()
    