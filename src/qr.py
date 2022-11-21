import numpy as np
from givens import *

def qr_decomposition(matrix):
    """Do QR decomposition to input square matrix

    Args:
        matrix (matrix): square matrix

    Returns:
        Tuple of matrix: Matrix Q and R, the result of decomposition of A 
    """
    size_matrix = len(matrix)
    q_transposed = np.identity(size_matrix)

    for m in range(0, size_matrix - 1):
        for n in range(m + 1, size_matrix):

            givens = givens_m_n_qr(matrix, m, n)
            # print(givens)
            q_transposed =  np.matmul(givens, q_transposed)

            matrix =  np.matmul(givens, matrix)
            # if matrix[n, m] < 1.0e-7:
            #     matrix[n, m] = 0
            # print(m)
            # print(n)
            # print(matrix)

    q = np.transpose(q_transposed)
    return (q, matrix)

def qr_iteration_with_accum_q(matrix, n: int):
    """Do QR iteration n times

    Args:
        matrix (matrix): square matrix
        n (int): number of iteration

    Returns:
        tuple of matrix: Result of iteration n times, and eigenvector matrix
    """
    accum_q = np.identity(len(matrix))
    for i in range(1, n+1):
        q, r = qr_decomposition(matrix)
        matrix = np.matmul(r, q)
        accum_q = np.matmul(accum_q, q)
    return matrix, accum_q