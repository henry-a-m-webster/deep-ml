import numpy as np


def cholesky_decomposition(A):
    A = np.array(A)
    rows, columns = np.shape(A)
    eigenvalues, eigenvectors = np.linalg.eig(A)
    L = np.zeros(np.shape(A))
    if rows != columns or any(eigenvalue < 0 for eigenvalue in eigenvalues) or not np.allclose(A, A.T):
        return -1
    else:
        for i in range(rows):
            for j in range(columns):
                if i == j:
                    L[i,i] = np.sqrt(A[i, i] - np.sum(L[i, :i]**2))
                elif i > j:
                    L[i, j] = 1/L[j,j]*(A[i, j] - np.sum(L[i, :j]*L[j, :j]))
    return L.astype(float).tolist()

    