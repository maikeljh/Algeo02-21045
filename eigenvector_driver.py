import numpy as np
from eigenvalue import get_real_eigenvalue, compute_eigenvalue_with_accum_q, get_k_eigenvalue_with_accum_q
from hessenberg import hessenberg_form
from qr import *
from eigenvector import get_k_eigenvector
import time

def main():
    np.set_printoptions(precision=3)
    matrix = np.loadtxt('driver_data\eigenvalue.txt', usecols=range(4))

    # print(matrix)

    # matrix = hessenberg_form(matrix)

    # print(hessenberg_matrix)

    time1 = time.time()
    result, q = compute_eigenvalue_with_accum_q(matrix)
    print(result)
    print(q)
    

    

    arr = get_k_eigenvector(result, q)
    time2 = time.time()
    print("Diperlukan waktu selama: ")

    print(time2 - time1)
    # np.set_printoptions(precision=3)
    # q = np.transpose(q)
    # hasil = np.matmul(matrix, q[0]) - q[0] * result[0]
    print(f"Didapat K eigenvector adalah")
    print(arr)

if __name__ == '__main__':
    main()

