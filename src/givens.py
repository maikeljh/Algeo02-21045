import numpy as np


def givens_template(m: int, n: int, k: int, c: float, s: float):
    """Return givens matrix, given the value of axis m and n
    and the value of k, c, s.

    Args:
        m (int): axis rotation of interest
        n (int): axis rotation of interest
        k (int): size of the givens matrix
        c (float): constant
        s (float): constant

    Returns:
        matrix: Givens matrix
    """
    identity = np.identity(k)
    identity[m, m] = c
    identity[n, n] = c
    identity[n, m] = -s
    identity[m, n] = s
    
    return identity

# TODO: Inget ganti-ganti ini
def givens_csr_hessenberg(input_matrix, m: int, n: int):
    """calculate the appropriate c and s constant to make givens matrix

    Args:
        input_matrix (matrix): input square matrix
        m (int): axis rotation of interest
        n (int): axis rotation of interest

    Returns:
        tuple : tuple of constant c and s
    """
    matrix = np.array(input_matrix)
    a = matrix[m][m - 1]
    b = matrix[n][m - 1]
    if b == 0:
        c = np.sign(a)
        if (c == 0):
            c = 1.0
        s = 0
    elif a == 0:
        c = 0
        s = np.sign(b)
    elif abs(a) > abs(b):
        t = b / a
        u = np.sign(a) * np.sqrt(1 + t * t)
        c = 1 / u
        s = c * t
    else:
        t = a / b
        u = np.sign(b) * np.sqrt(1 + t * t)
        s = 1 / u
        c = s * t
    return (c, s)
# TODO: Inget ganti-ganti ini
def givens_csr_qr(input_matrix, m: int, n: int):
    """Calculate the appropriate c and s constant to make givens matrix

    Args:
        input_matrix (matrix): input square matrix
        m (int): axis rotation of interest
        n (int): axis rotation of interest

    Returns:
        tuple : tuple of constant c and s
    """
    matrix = np.array(input_matrix)
    a = matrix[m][m]
    b = matrix[n][m]
    if b == 0:
        c = np.sign(a)
        if (c == 0):
            c = 1.0
        s = 0
    elif a == 0:
        c = 0
        s = np.sign(b)
    elif abs(a) > abs(b):
        t = b / a
        u = np.sign(a) * np.sqrt(1 + t * t)
        c = 1 / u
        s = c * t
    else:
        t = a / b
        u = np.sign(b) * np.sqrt(1 + t * t)
        s = 1 / u
        c = s * t
    return (c, s)

def givens_m_n_hessenberg (matrix, m: int, n: int):
    """Get givens matrix to make hessenberg form 


    Args:
        matrix (matrix): matriks 
        m (int): axis rotation of interest
        n (int): axis rotation of interest

    Returns:
        matriks: givens matrix to make hessenberg form
    """
    k = len(matrix)
    c, s = givens_csr_hessenberg(matrix, m, n)
    givens_matrix = givens_template(m, n, k, c, s)

    return givens_matrix

def givens_m_n_qr (matrix, m: int, n: int):
    """Get givens matrix for qr decomposition


    Args:
        matrix (matrix): matriks 
        m (int): axis rotation of interest
        n (int): axis rotation of interest

    Returns:
        matriks: givens matrix for qr decomposition
    """
    k = len(matrix)
    c, s = givens_csr_qr(matrix, m, n)
    givens_matrix = givens_template(m, n, k, c, s)

    return givens_matrix
    

