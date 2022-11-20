import numpy as np
from qr import *

def main():
    matrix = np.loadtxt('driver_data\hessenberg.txt', usecols=range(6))

    print(matrix)

    # q, r = qr_decomposition(matrix)

    # print("HASILL")
    # print(q)
    # print(r)
    # hasil = np.matmul(q, r)
    # print(hasil)

    hasil = qr_iteration(matrix, 100)

    np.set_printoptions(precision=3)
    print(hasil)

if __name__ == '__main__':
    main()

