import numpy as np
from givens import givens_m_n_hessenberg

def hessenberg_form(matrix):
    size_matrix = len(matrix)

    for m in range(1, size_matrix - 1):
        for n in range(m + 1, size_matrix):
            givens = givens_m_n_hessenberg(matrix, m, n)
            # print(givens)
            transposed_givens = np.transpose(givens)
            # print(transposed_givens)
            matrix =  np.matmul(givens, matrix)
            matrix =  np.matmul(matrix, transposed_givens)
            if matrix[n, m-1] < 1.0e-13:
                matrix[n, m-1] = 0
            # print(m)
            # print(n)

    return matrix