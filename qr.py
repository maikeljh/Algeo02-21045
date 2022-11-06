import numpy as np
from givens import *

def qr_decomposition(matrix):
    size_matrix = len(matrix)
    q_transposed = np.identity(size_matrix)

    for m in range(0, size_matrix - 1):
        for n in range(m + 1, size_matrix):

            givens = givens_m_n_qr(matrix, m, n)
            # print(givens)
            q_transposed =  np.matmul(givens, q_transposed)

            matrix =  np.matmul(givens, matrix)
            if matrix[n, m] < 1.0e-13:
                matrix[n, m] = 0
            # print(m)
            # print(n)
            # print(matrix)

    q = np.transpose(q_transposed)
    return (q, matrix)

def qr_iteration(a, n):
    for i in range(1, n+1):
        q, r = qr_decomposition(a)
        a = np.matmul(r, q)
    return a