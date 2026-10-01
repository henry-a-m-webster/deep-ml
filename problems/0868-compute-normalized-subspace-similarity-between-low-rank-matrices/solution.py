import numpy as np

def subspace_similarity(A: list, B: list, i: int, j: int) -> float:
    """
    Compute the normalized subspace similarity between the top-i left singular
    subspace of A and the top-j left singular subspace of B.

    Args:
        A: matrix as a list of lists
        B: matrix as a list of lists (same number of rows as A)
        i: number of top left singular vectors to take from A
        j: number of top left singular vectors to take from B

    Returns:
        A float in [0, 1] measuring subspace similarity.
    """
    A, B = np.array(A), np.array(B)
    U_A, S_A, Vh_A = np.linalg.svd(A)
    U_B, S_B, Vh_B = np.linalg.svd(B)

    U_Ai = U_A[:, :i]
    U_Bj = U_B[:, :j]

    return ((np.linalg.norm(U_Ai.T @ U_Bj, ord = 'fro'))**2)/min(i, j)

    
