import numpy as np


def givens_template(m: int, n: int, k: int, c: float, s: float):
    identity = np.identity(k)
    identity[m, m] = c
    identity[n, n] = c
    identity[n, m] = -s
    identity[m, n] = s
    
    return identity

# TODO: Inget ganti-ganti ini
def givens_csr_hessenberg(input_matrix, m: int, n: int):
    matrix = np.array(input_matrix)
    a = matrix[m][m - 1]
    b = matrix[n][m - 1]
    if b == 0:
        c = np.sign(a)
        if (c == 0):
            c = 1.0
        s = 0
        r = abs(a)
    elif a == 0:
        c = 0
        s = np.sign(b)
        r = abs(b)
    elif abs(a) > abs(b):
        t = b / a
        u = np.sign(a) * np.sqrt(1 + t * t)
        c = 1 / u
        s = c * t
        r = a * u
    else:
        t = a / b
        u = np.sign(b) * np.sqrt(1 + t * t)
        s = 1 / u
        c = s * t
        r = b * u
    return (c, s, r)
# TODO: Inget ganti-ganti ini
def givens_csr_qr(input_matrix, m: int, n: int):
    matrix = np.array(input_matrix)
    a = matrix[m][m]
    b = matrix[n][m]
    if b == 0:
        c = np.sign(a)
        if (c == 0):
            c = 1.0
        s = 0
        r = abs(a)
    elif a == 0:
        c = 0
        s = np.sign(b)
        r = abs(b)
    elif abs(a) > abs(b):
        t = b / a
        u = np.sign(a) * np.sqrt(1 + t * t)
        c = 1 / u
        s = c * t
        r = a * u
    else:
        t = a / b
        u = np.sign(b) * np.sqrt(1 + t * t)
        s = 1 / u
        c = s * t
        r = b * u
    return (c, s, r)

def givens_m_n_hessenberg (matrix, m: int, n: int):
    k = len(matrix)
    c, s, r = givens_csr_hessenberg(matrix, m, n)
    givens_matrix = givens_template(m, n, k, c, s)

    return givens_matrix

def givens_m_n_qr (matrix, m: int, n: int):
    k = len(matrix)
    c, s, r = givens_csr_qr(matrix, m, n)
    givens_matrix = givens_template(m, n, k, c, s)

    return givens_matrix
    

