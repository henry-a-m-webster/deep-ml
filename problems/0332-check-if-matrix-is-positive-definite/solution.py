import numpy as np

def check_positive_definite(matrix: list) -> dict:
    eigenvalues, eigenvectors= np.linalg.eig(np.array(matrix))
    eigenvalues = np.round(eigenvalues.astype(float), 4)
    if any(eigenvalue < 1e-10 for eigenvalue in eigenvalues): 
        positive_definite = False
    else:
        positive_definite = True
    output = {'is_positive_definite': positive_definite, 'eigenvalues' : sorted(eigenvalues.tolist())}
    return output
    