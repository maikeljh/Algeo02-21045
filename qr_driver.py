import numpy as np
from qr import qr_decomposition

def main():
    matrix = np.loadtxt('driver_data\hessenberg.txt', usecols=range(4))

    print(matrix)

    q, r = qr_decomposition(matrix)

    print("HASILL")
    print(q)
    print(r)
    hasil = np.matmul(q, r)
    print(hasil)

if __name__ == '__main__':
    main()

