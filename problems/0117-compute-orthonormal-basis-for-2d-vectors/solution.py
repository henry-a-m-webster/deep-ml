import numpy as np

def orthonormal_basis(vectors: list[list[float]], tol: float = 1e-10) -> list[np.ndarray]:
    output = []
    for i in range(len(vectors)):
        v = np.array(vectors[i])
        sum_proj = sum(np.dot(v, u)*u for u in output) if output else 0
        w = v - sum_proj
        if np.linalg.norm(w) > tol:
            output.append(w/np.linalg.norm(w))
    return output
            