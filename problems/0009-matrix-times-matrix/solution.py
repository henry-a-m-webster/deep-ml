import numpy as np

def matrixmul(a: list[list[int|float]], b: list[list[int|float]]) -> list[list[int|float]]:
    if np.shape(np.array(a))[1] == np.shape(np.array(b))[0]:
        A = np.array(a)
        B = np.array(b)
        return (A @ B).tolist()
    else:
        return -1