import numpy as np
from eigenvalue import get_real_eigenvalue, compute_eigenvalue_with_accum_q
from hessenberg import hessenberg_form
from qr import *

def main():
    np.set_printoptions(precision=3)
    matrix = np.loadtxt('driver_data\eigenvalue.txt', usecols=range(6))

    # print(matrix)

    # print(hessenberg_matrix)

    result, q = compute_eigenvalue_with_accum_q(matrix)

    np.set_printoptions(precision=3)
    print(result)
    print(q)

if __name__ == '__main__':
    main()

