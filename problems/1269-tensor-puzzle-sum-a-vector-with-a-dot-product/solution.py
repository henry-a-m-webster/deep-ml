import numpy as np

def vector_sum(a: np.ndarray):
    length = len(a)
    ones = (np.arange(length) * 0) + 1
    output = ones @ a
    return output
